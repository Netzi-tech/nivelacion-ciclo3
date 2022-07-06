from django.db import models
from django.utils import timezone

class Especialidad(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True
    )
    createdAt = models.DateField(
        null=False,
        blank=False,
        auto_now_add = True
    )
    lastChangeDate = models.DateTimeField(
        null=True,
        blank=False,
        auto_now = True
    )
    isActive = models.BooleanField(
        null=False,
        blank=False,
        default=True
    )