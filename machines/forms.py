from django import forms
from .models import Machine


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['name', 'machine_type',  'description', 'last_maintenance']
        MACHINE_TYPE_CHOICES = (
            ('', 'Select an age'),
            ('S', 'Süblimasyon'),
            ('D', 'Dtf'),
            ('U', 'Uv'),
        )
        widgets = {
            'machine_type': forms.Select(choices=MACHINE_TYPE_CHOICES),
        }
