# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0009_auto_20161027_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='num2',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
