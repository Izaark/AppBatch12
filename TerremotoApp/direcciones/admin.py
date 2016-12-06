from django.contrib import admin
from .models import *

# class DireccionAdmin(admin.ModelAdmin):
#     model = Direccion
#     fieldsets = (
#         ('Direccion postal', {'fields': (
#         	('calle','numero_exterior','numero_interior'),
#         	('codigo_postal','nombre','municipio'),
#         	('ciudad','estado','pais'),
#         	)}),
#         ('Coordenadas', {'fields': (
#         	('utm_este', 'utm_norte'),
#         	('enlace_mapa')
#             )}),
#         )

admin.site.register(Direccion)
admin.site.register(Telefono)