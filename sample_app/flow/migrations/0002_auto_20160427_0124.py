# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-27 01:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['step_number']},
        ),
    ]
