# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-16 03:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direcciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colonia',
            name='ciudad',
            field=models.CharField(default='', max_length=128, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='colonia',
            name='codigo_postal',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='colonia',
            name='estado',
            field=models.CharField(default='DF', max_length=60, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='colonia',
            name='municipio',
            field=models.CharField(default='', max_length=60, verbose_name='Delegacion o municipio'),
        ),
        migrations.AlterField(
            model_name='colonia',
            name='nombre',
            field=models.CharField(default='', max_length=300, verbose_name='Colonia'),
        ),
        migrations.AlterField(
            model_name='colonia',
            name='pais',
            field=models.CharField(default='Mexico', max_length=300, verbose_name='Pais'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='calle',
            field=models.CharField(default='', max_length=220, verbose_name='Calle'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='calle_y_numero',
            field=models.CharField(default='', editable=False, max_length=300, verbose_name='Calle y numero'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='enlace_mapa',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='numero_exterior',
            field=models.CharField(default='', max_length=40, verbose_name='Numero exterior'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='numero_interior',
            field=models.CharField(blank=True, default='', max_length=40, verbose_name='Numero interior'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='utm_este',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=11, verbose_name='Coordenadas UTM-E'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='utm_norte',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=11, verbose_name='Coordenadas UTM-N'),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='numero_telefono',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]