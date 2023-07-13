from django.shortcuts import render, redirect
from work_orders.models import WorkOrder
from datetime import date
from django.contrib.auth.decorators import login_required


@login_required
def transactions(request, work_order_uuid):
    work_order = WorkOrder.objects.get(uuid=work_order_uuid)

    context = {
        'work_order': work_order
    }
    if work_order.status == 'completed' or work_order.status == 'cancelled':
        return redirect('work_order_detail', work_order_pk=work_order.id)

    return render(request, 'work_orders/process.html', context)


@login_required
def start_process(request, work_order_uuid):
    work_order = WorkOrder.objects.get(uuid=work_order_uuid)
    work_order.status = 'in_progress'
    work_order.actual_start_date = date.today()
    work_order.processed_by = request.user
    work_order.save()

    return redirect('work_order_detail', work_order_pk=work_order.id)


@login_required
def pause_process(request, work_order_uuid):
    work_order = WorkOrder.objects.get(uuid=work_order_uuid)
    work_order.status = 'paused'
    work_order.save()

    return redirect('work_order_detail', work_order_pk=work_order.id)


@login_required
def continue_process(request, work_order_uuid):
    work_order = WorkOrder.objects.get(uuid=work_order_uuid)
    work_order.status = 'in_progress'
    work_order.save()

    return redirect('work_order_detail', work_order_pk=work_order.id)


@login_required
def complete_process(request, work_order_uuid):
    work_order = WorkOrder.objects.get(uuid=work_order_uuid)
    work_order.status = 'completed'
    work_order.actual_end_date = date.today()
    work_order.save()

    return redirect('work_order_detail', work_order_pk=work_order.id)


@login_required
def cancel_process(request, work_order_uuid):
    if request.user.is_superuser:
        work_order = WorkOrder.objects.get(uuid=work_order_uuid)
        work_order.status = 'cancelled'
        work_order.save()

    return redirect('work_order_detail', work_order_pk=work_order.id)


@login_required
def copy_complete_process(request, work_order_uuid, number_of_remained_copy):
    work_order = WorkOrder.objects.get(uuid=work_order_uuid)

    work_order.number_of_remained_copy = float(number_of_remained_copy)
    work_order.remained_amount = work_order.number_of_remained_copy * work_order.number_of_blocks

    if not work_order.actual_start_date:
        work_order.actual_start_date = date.today()

    if not work_order.processed_by:
        work_order.processed_by = request.user

    if work_order.status == 'waiting':
        work_order.status = 'in_progress'
        work_order.actual_start_date = date.today()

    if work_order.number_of_remained_copy < 0:
        work_order.number_of_remained_copy = 0
        work_order.status = 'completed'
        work_order.actual_end_date = date.today()

    work_order.save()

    return redirect('work_order_detail', work_order_pk=work_order.id)

