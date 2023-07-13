from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def operator_list(request):
    operators = User.objects.filter(is_superuser=False).order_by('first_name')

    context = {
        'operators': operators
    }

    return render(request, 'operators/list.html', context)
