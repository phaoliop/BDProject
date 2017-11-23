# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Proyecto
from .models import ProyectoDocs
from .models import Distrito
from .models import Provincia
from .models import Departamento
from .models import Cliente
from .models import Persona
from .models import Profesion
from .models import PersonaProf
from .models import Fase
from .models import Estado
from .models import ProyectoCosto
from .models import Experiencia
from .models import Persona_TICS
from .models import TICS

# Register your models here.

admin.site.register(Proyecto)             
admin.site.register(ProyectoDocs)
admin.site.register(Distrito)
admin.site.register(Provincia)
admin.site.register(Departamento)
admin.site.register(Cliente)
admin.site.register(Persona)
admin.site.register(Profesion)
admin.site.register(PersonaProf)
admin.site.register(Fase)
admin.site.register(Estado)
admin.site.register(ProyectoCosto)
admin.site.register(Experiencia)
admin.site.register(Persona_TICS)
admin.site.register(TICS)

