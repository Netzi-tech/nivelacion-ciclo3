from django.db import models
from django.utils import timezone
from .persona import Persona

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    fk_persona = models.ForeignKey(
        Persona,
        on_delete=models.RESTRICT,
        null=False
    )
    direccion = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    ciudad = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    fech_naci = models.DateTimeField(
        null=False,
        blank=False,
        auto_now = True
    )
    latitud = models.DecimalField(
        max_digits=10, 
        decimal_places=8,
        null=True,
        default=None
    )
    longitud = models.DecimalField(
        max_digits=10, 
        decimal_places=8,
        null=True,
        default=None
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