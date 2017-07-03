# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-14 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0004_auto_20170614_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmenthistorymodel',
            name='appointment_start_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='appointmenthistorymodel',
            name='duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appointmenthistorymodel',
            name='patient_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appointmenthistorymodel',
            name='session_end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='appointmenthistorymodel',
            name='session_start_time',
            field=models.DateTimeField(null=True),
        ),
    ]