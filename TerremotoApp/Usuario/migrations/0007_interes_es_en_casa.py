# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-21 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0006_auto_20161121_0643'),
    ]

    operations = [
        migrations.AddField(
            model_name='interes',
            name='es_en_casa',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
