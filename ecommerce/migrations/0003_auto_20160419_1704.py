# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_auto_20160419_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impuestos',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
    ]
