from django.db import models
from django.utils import timezone

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    identificacion = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        unique=True
    )
    nombres = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    apellidos = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    telefono = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    genero = models.CharField(
        max_length=1,
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