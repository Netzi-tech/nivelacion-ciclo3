from django.db import models
from django.utils import timezone
from .persona import Persona
from .especialidad import Especialidad

class Medico(models.Model):
    id = models.AutoField(primary_key=True)
    fk_persona = models.ForeignKey(
        Persona,
        on_delete=models.RESTRICT,
        null=False
    )
    fk_especialidad = models.ForeignKey(
        Especialidad,
        on_delete=models.RESTRICT,
        null=False
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