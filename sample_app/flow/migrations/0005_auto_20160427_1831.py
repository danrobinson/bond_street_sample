# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-27 18:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0004_auto_20160427_1141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['number']},
        ),
        migrations.RenameField(
            model_name='step',
            old_name='step_number',
            new_name='number',
        ),
    ]