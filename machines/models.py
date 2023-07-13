from django.db import models
from utils.models import StarterModel


class Machine(StarterModel):
    name = models.CharField(max_length=100)
    MACHINE_CHOICES = (
        ('S', 'Süblimasyon'),
        ('D', 'Dtf'),
        ('U', 'Uv'),
    )
    machine_type = models.CharField(max_length=1, choices=MACHINE_CHOICES)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_maintenance = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Makineler"
