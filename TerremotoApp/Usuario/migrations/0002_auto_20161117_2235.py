# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-17 22:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='_direccion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='direcciones.Direccion', verbose_name='direccion'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='circulo_amigos',
            field=models.ManyToManyField(blank=True, related_name='_usuario_circulo_amigos_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.ManyToManyField(blank=True, to='direcciones.Telefono', verbose_name='telefono'),
        ),
    ]
