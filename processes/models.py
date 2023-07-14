from django.db import models
from utils.models import StarterModel
from work_orders.models import WorkOrder
from django.contrib.auth.models import User


class ProcessLog(StarterModel):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, default=4)
    process = models.CharField(max_length=200)
    remained_amount = models.IntegerField()
    number_of_remained_copy = models.DecimalField(max_digits=5, decimal_places=1)
    log_date_time = models.DateTimeField(auto_now_add=True)
    processed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="processed_by",
                                     null=False, blank=False)

    def __str__(self):
        return self.process

    class Meta:
        verbose_name_plural = "İşlem Logları"
