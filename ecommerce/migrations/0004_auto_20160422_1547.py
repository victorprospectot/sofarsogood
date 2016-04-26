# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20160419_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatAPIPaypal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('url_paypal', models.URLField()),
                ('version', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CatOperacionesAPIPaypal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo', models.CharField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CatTipoEntorno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CuentaPaypal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apiusername', models.EmailField(max_length=254)),
                ('_apipassword', models.TextField(db_column='apipassword')),
                ('_apisignature', models.TextField(db_column='apisignature')),
                ('habilitado', models.BooleanField(default=False)),
                ('receiver_email', models.EmailField(max_length=254, unique=True)),
                ('cat_apipaypal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.CatAPIPaypal')),
                ('cat_tipoentorno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.CatTipoEntorno')),
            ],
        ),
        migrations.CreateModel(
            name='EstadosPayPal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='OpcionesAPIPaypalOperaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_field', models.CharField(max_length=80)),
                ('value', models.CharField(max_length=2048)),
                ('habilitado', models.BooleanField(default=False)),
                ('catapipaypal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.CatAPIPaypal')),
                ('catoperacionesapipaypal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.CatOperacionesAPIPaypal')),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='valido_hasta',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='catapipaypal',
            name='cat_tipoentorno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.CatTipoEntorno'),
        ),
        migrations.AddField(
            model_name='catapipaypal',
            name='operaciones',
            field=models.ManyToManyField(through='ecommerce.OpcionesAPIPaypalOperaciones', to='ecommerce.CatOperacionesAPIPaypal'),
        ),
        migrations.AlterUniqueTogether(
            name='opcionesapipaypaloperaciones',
            unique_together=set([('catapipaypal', 'catoperacionesapipaypal', 'request_field')]),
        ),
    ]