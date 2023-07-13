from django.db import models
from utils.models import StarterModel
from machines.models import Machine
from django.contrib.auth.models import User
import uuid


class WorkOrder(StarterModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    form = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField()
    remained_amount = models.IntegerField(default=0)
    number_of_blocks = models.IntegerField()
    number_of_copy = models.DecimalField(max_digits=5, decimal_places=1)
    number_of_remained_copy = models.DecimalField(max_digits=5, decimal_places=1)
    priority = models.CharField(default="low", max_length=20)
    status = models.CharField(default="waiting", max_length=20)
    planned_start_date = models.DateField()
    planned_end_date = models.DateField()
    actual_start_date = models.DateField(null=True, blank=True)
    actual_end_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="work_orders_created_by")
    processed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="work_orders_processed_by",
                                     null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "İş Emirleri"
