from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User
from direcciones.models import *
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    _direccion = models.ForeignKey(Direccion, verbose_name='dirección', null=True)
    telefono = models.ManyToManyField(Telefono, verbose_name='teléfono')
    profesion = models.CharField(max_length=140, blank=True, null=True)
    circulo_amigos = models.ManyToManyField('self', related_name='usuario_amigos')

    def __str__(self):
    	return "{0} {1}".format(self.first_name, self.last_name)