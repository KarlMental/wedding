# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='rsvp',
            field=models.CharField(max_length=40),
        ),
    ]
