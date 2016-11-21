from django.db import models
from django.utils.text import slugify
from django.core.validators import RegexValidator
from datetime import datetime


class Colonia(models.Model):
    codigo_postal = models.CharField(
        max_length=11, default='', blank=False, null=False)
    nombre = models.CharField(
        'Colonia', max_length=300, default='', null=False, blank=False)
    municipio = models.CharField(
        'Delegacion o municipio', max_length=60, default='',
         blank=False, null=False)
    ciudad = models.CharField(
        'Ciudad', max_length=128, default='', blank=False, null=False)
    estado = models.CharField(
        'Estado', max_length=60, default='DF', blank=False, null=False)
    pais = models.CharField(
        'Pais', default='Mexico', max_length=300, blank=False, null=False)

    def __str__(self):
        return "{0}{1}".format(self.id, self.nombre)

class Meta:
    abstract = True


class Direccion(Colonia):
    slug = models.SlugField(max_length=300)
    calle_y_numero = models.CharField(
        'Calle y numero', max_length=300, null=False, blank=False, default='',
         editable=False)
    calle = models.CharField(
        'Calle', max_length=220, null=False, blank=False, default='')
    numero_exterior = models.CharField(
        'Numero exterior', max_length=40, null=False, blank=False, default='')
    numero_interior = models.CharField(
        'Numero interior', max_length=40, null=False, blank=True, default='')
    longitud = models.DecimalField('Coordenadas UTM-E', max_digits=17,
        decimal_places=14, null=False, blank=True, default=0)
    latitud = models.DecimalField('Coordenadas UTM-N', max_digits=17,
        decimal_places=14, null=False, blank=True, default=0)
    enlace_mapa = models.URLField(blank=True, null=False, default='')

    creado_el = models.DateTimeField(default=datetime.now, editable=False)
    modificado_el = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Direcciones'

    def __str__(self):
        return(self.calle_y_numero)

    def save(self, *args, **kwargs):
        self.calle_y_numero = "{0} {1} {2}".format(
            self.calle, self.numero_exterior, self.numero_interior)
        if not self.id:
            self.creado_el = datetime.now()
            self.slug = slugify(self.nombre)
        super(Direccion, self).save(*args, **kwargs)


class Telefono(models.Model):
    telefono_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    numero_telefono = models.CharField(
        validators=[telefono_regex],
        blank=True, max_length=17)  # validators should be a list

    def __str__(self):
        return(self.numero_telefono)