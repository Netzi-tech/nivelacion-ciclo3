from django.contrib import admin

# Register your models here.
from .models.persona import Persona
from .models.paciente import Paciente
from .models.parentesco import Parentesco
from .models.familia import Familia
from .models.especialidad import Especialidad
from .models.medico import Medico
from .models.hospitalizacion import Hospitalizacion
from .models.registro_signos import RegistroASignos

admin.site.register(Persona)
admin.site.register(Paciente)
admin.site.register(Parentesco)
admin.site.register(Familia)
admin.site.register(Especialidad)
admin.site.register(Medico)
admin.site.register(Hospitalizacion)
admin.site.register(RegistroASignos)