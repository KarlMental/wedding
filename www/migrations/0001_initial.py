# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('rsvp', models.BooleanField()),
                ('email', models.EmailField(max_length=100)),
                ('dietary_restrictions', models.TextField()),
                ('shuttle', models.CharField(max_length=40)),
            ],
        ),
    ]