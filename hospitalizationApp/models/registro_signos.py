from django.db import models
from django.utils import timezone
from .medico import Medico
from .hospitalizacion import Hospitalizacion

class RegistroASignos(models.Model):
    id = models.AutoField(primary_key=True)
    fk_medico = models.ForeignKey(
        Medico,
        on_delete=models.RESTRICT,
        null=False
    )
    fk_hospitalizacion = models.ForeignKey(
        Hospitalizacion,
        on_delete=models.RESTRICT,
        null=False
    )
    oximetria = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        null=False
    )
    frec_resp = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        null=False
    )
    frec_card = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        null=False
    )
    temperatura = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        null=False
    )
    prec_arte = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        null=False
    )
    glicemias = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
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