# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisitos', '0003_auto_20171202_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objetivo',
            name='estabilidad',
            field=models.CharField(choices=[('PD', 'PD'), ('Importante', 'Importante'), ('Vital', 'Vital')], default='PD', max_length=15),
        ),
        migrations.AlterField(
            model_name='objetivo',
            name='estado',
            field=models.CharField(choices=[('PD', 'PD'), ('Importante', 'Importante'), ('Vital', 'Vital')], default='PD', max_length=15),
        ),
        migrations.AlterField(
            model_name='objetivo',
            name='importancia',
            field=models.CharField(choices=[('PD', 'PD'), ('Importante', 'Importante'), ('Vital', 'Vital')], default='PD', max_length=15),
        ),
        migrations.AlterField(
            model_name='objetivo',
            name='urgencia',
            field=models.CharField(choices=[('PD', 'PD'), ('Importante', 'Importante'), ('Vital', 'Vital')], default='PD', max_length=15),
        ),
    ]
