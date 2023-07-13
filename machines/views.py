from django.shortcuts import render, redirect
from .models import Machine
from .forms import MachineForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required


@login_required
def machine_list(request):
    machines = Machine.objects.all().order_by('created_date')

    context = {
        'machines': machines
    }

    return render(request, 'machines/list.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def machine_create(request):
    form = MachineForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

        return redirect('machine_list')

    context = {
        'form': form
    }
    return render(request, "machines/create.html", context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def machine_edit(request, machine_pk):
    machine = Machine.objects.get(pk=machine_pk)
    form = MachineForm(request.POST or None, instance=machine)

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect('machine_list')

    context = {
        'machine': machine,
        'form': form
    }

    return render(request, "machines/create.html", context)

