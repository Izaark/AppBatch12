from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User
from direcciones.models import *
from django.contrib.auth.models import AbstractUser


class Interes (models.Model):
    nombre = models.CharField(max_length=140)
    es_exterior = models.BooleanField()
    es_fisico = models.BooleanField()
    es_gratis = models.BooleanField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Interés'
        verbose_name_plural = 'Intereses'


class Usuario(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    _direccion = models.ForeignKey(
        Direccion, verbose_name='direccion', null=True)
    telefono = models.ManyToManyField(
        Telefono, verbose_name='telefono', blank=True)
    circulo_amigos = models.ManyToManyField(
        'self', related_name='amigos_usuario', blank=True)
    intereses = models.ManyToManyField(
        Interes, related_name='intereses_usuario', blank=True)

    def __str__(self):
        if self.first_name:
            return "{0} {1}".format(self.first_name, self.last_name)
        else:
            return self.username