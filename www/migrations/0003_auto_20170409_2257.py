# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 20:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_auto_20170409_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='rsvp',
            new_name='rsvp_answer',
        ),
        migrations.AddField(
            model_name='guest',
            name='rsvp_datetime',
            field=models.TimeField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
