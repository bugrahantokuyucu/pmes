from django.db import models
from utils.models import StarterModel
from work_orders.models import WorkOrder


class Note(StarterModel):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    note = models.TextField()

    def __str__(self):
        return self.work_order.title

    class Meta:
        verbose_name_plural = "Notlar"
