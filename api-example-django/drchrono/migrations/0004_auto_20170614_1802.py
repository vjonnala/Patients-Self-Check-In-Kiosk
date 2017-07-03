# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-14 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drchrono', '0003_delete_userdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentHistoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_id', models.IntegerField()),
                ('statusTime', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['-statusTime'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='appointmenthistorymodel',
            unique_together=set([('appointment_id', 'statusTime')]),
        ),
    ]
