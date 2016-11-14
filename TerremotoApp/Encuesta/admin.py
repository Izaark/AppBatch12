from django.contrib import admin

from .models import Pregunta, Cuestionario, Respuesta 
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Cuestionario)
