# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-03 16:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bars', '0002_bars_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bars',
            new_name='BarsLocation',
        ),
    ]
