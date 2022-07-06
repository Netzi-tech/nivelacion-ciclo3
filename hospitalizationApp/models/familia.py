from django.db import models
from django.utils import timezone
from .persona import Persona
from .paciente import Paciente
from .parentesco import Parentesco

class Familia(models.Model):
    id = models.AutoField(primary_key=True)
    fk_persona = models.ForeignKey(
        Persona,
        on_delete=models.RESTRICT,
        null=False
    )
    fk_paciente = models.ForeignKey(
        Paciente,
        on_delete=models.RESTRICT,
        null=False
    )
    fk_parentesco = models.ForeignKey(
        Parentesco,
        on_delete=models.RESTRICT,
        null=False
    )
    email = models.EmailField(
        max_length=255,
        null=False,
        blank=True,
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