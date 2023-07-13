# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import WorkOrder
from machines.models import Machine
from notes.models import Note
from .forms import WorkOrderForm
from qrcode import *
from io import BytesIO
from django.http import FileResponse, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
import locale
import base64
from datetime import date
from django.contrib.auth.decorators import login_required


@login_required
def work_order_list(request):
    work_orders = WorkOrder.objects.all().order_by('-created_date')
    js_list = []
    # status: complete, delayed, in_progress
    for work_order in work_orders:

        if date.today() > work_order.planned_end_date and work_order.status != 'complete':
            work_order.status = 'delayed'

        wo_dict = work_order.__dict__
        js_dict = {
            "id": wo_dict['id'],
            "title": wo_dict['title'],
            "date": str(wo_dict['planned_start_date'].strftime("%d %B %Y")),
            "description": wo_dict['description'],
            "descriptionText": wo_dict['description'],
            "status": wo_dict['status'],
            "priority": wo_dict['priority'],
        }
        js_list.append(js_dict)

    context = {
        'work_orders': work_orders,
        'js_list': js_list,
    }
    return render(request, 'work_orders/list.html', context)


@login_required
def generate_qr(request, work_order_uuid):
    img = make(request.get_host() + '/work_orders/' + str(work_order_uuid))
    return img


@login_required
@user_passes_test(lambda u: u.is_superuser)
def work_order_create(request):
    form = WorkOrderForm(request.POST or None, request.FILES or None)
    machines = Machine.objects.all()

    if form.is_valid():
        new_work_order = form.save(commit=False)
        new_work_order.remained_amount = new_work_order.amount
        new_work_order.number_of_copy = new_work_order.amount / new_work_order.number_of_blocks
        new_work_order.number_of_remained_copy = new_work_order.number_of_copy
        new_work_order.created_by = request.user
        new_work_order.save()
        work_order_pk = new_work_order.pk

        return HttpResponseRedirect('/work_orders/{0}'.format(work_order_pk))

    context = {
        'form': form,
        'machines': machines,
    }
    return render(request, "work_orders/create.html", context)


@login_required
def work_order_detail(request, work_order_pk):
    work_order = WorkOrder.objects.get(pk=work_order_pk)
    notes = Note.objects.filter(work_order=work_order)
    qr = generate_qr(request, work_order_uuid=work_order.uuid)

    buffer_png = BytesIO()
    qr.save(buffer_png, kind='PNG')

    completion_rate = 100 - (work_order.number_of_remained_copy / work_order.number_of_copy) * 100

    if completion_rate == 100:
        work_order.status = 'completed'
        work_order.save()

    context = {
        'work_order': work_order,
        'notes': notes,
        'qr_str': base64.b64encode(buffer_png.getvalue()).decode('utf-8'),
        'completion_rate': int(completion_rate),
    }
    return render(request, 'work_orders/detail.html', context)


@user_passes_test(lambda u: u.is_superuser)
@login_required
def work_order_edit(request, work_order_pk):
    work_order = WorkOrder.objects.get(pk=work_order_pk)
    machines = Machine.objects.all()
    form = WorkOrderForm(request.POST or None, instance=work_order)

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect('work_order_detail', work_order_pk=work_order_pk)

    context = {
        'work_order': work_order,
        'machines': machines,
        'form': form
    }

    return render(request, "work_orders/create.html", context)


@login_required
def create_pdf(request, work_order_pk):
    x = 100
    y = 800
    locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')

    work_order = WorkOrder.objects.get(pk=work_order_pk)

    buffer = BytesIO()
    pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
    p = canvas.Canvas(buffer, pagesize=A4)

    p.setFont("Verdana", 14)
    p.drawString(x, y, "BASKI TAKİP FORMU")
    p.drawString(x, y-60, "İş Emri: {}".format(work_order.title))
    p.drawString(x, y-90, "Baskı Makinesi: {}".format(work_order.machine.name))
    p.drawString(x, y-120, "Başlangıç Tarihi: {}".format(work_order.planned_start_date.strftime("%d %B %Y")))
    p.drawString(x, y-150, "Bitiş Tarihi: {}".format(work_order.planned_end_date.strftime("%d %B %Y")))
    p.drawString(x, y - 180, "Beden: {}".format(work_order.form))
    p.drawString(x, y - 210, "Basılacak Adet: {}".format(work_order.amount))
    p.drawString(x, y - 240, "Baskı Blok Sayısı: {}".format(work_order.number_of_blocks))
    p.drawString(x, y - 270, "Kopya Sayısı: {}".format(work_order.number_of_copy))

    qr_image = generate_qr(request, work_order_uuid=work_order.uuid)
    y = y - 500
    p.drawInlineImage(qr_image, x, y, width=200, height=200)

    p.showPage()
    p.save()
    buffer.seek(0)
    file_name = "{0}-{1}.pdf".format(work_order.planned_start_date, work_order.title)
    return FileResponse(buffer, as_attachment=True, filename=file_name)
