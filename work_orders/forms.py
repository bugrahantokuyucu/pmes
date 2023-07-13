from django.forms import ModelForm
from .models import WorkOrder


class WorkOrderForm(ModelForm):
    class Meta:
        model = WorkOrder
        fields = ['machine',
                  'title',
                  'description',
                  'form',
                  'amount',
                  'number_of_blocks',
                  'planned_start_date',
                  'planned_end_date']
