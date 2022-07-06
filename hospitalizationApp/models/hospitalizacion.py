from django.db import models
from django.utils import timezone
from .medico import Medico
from .paciente import Paciente

class Hospitalizacion(models.Model):
    id = models.AutoField(primary_key=True)
    fk_medico = models.ForeignKey(
        Medico,
        on_delete=models.RESTRICT,
        null=False
    )
    fk_paciente = models.ForeignKey(
        Paciente,
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