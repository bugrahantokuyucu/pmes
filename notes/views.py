from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from work_orders.models import WorkOrder
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required


@login_required
def note_list(request):
    notes = Note.objects.all().order_by('created_date')

    context = {
        'notes': notes
    }

    return render(request, 'notes/list.html', context)


@login_required
def note_create(request):
    form = NoteForm(request.POST or None, request.FILES or None)
    work_orders = WorkOrder.objects.all()

    if form.is_valid():
        form.save()

        return redirect('note_list')

    context = {
        'form': form,
        'work_orders': work_orders
    }
    return render(request, "notes/create.html", context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def note_edit(request, pk):
    note = Note.objects.get(pk=pk)
    form = NoteForm(request.POST or None, instance=note)

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect('note_list')

    context = {
        'note': note,
        'form': form
    }

    return render(request, "notes/create.html", context)

