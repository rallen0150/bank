# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0011_auto_20161027_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='balance',
        ),
        migrations.AddField(
            model_name='transaction',
            name='num3',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='num2',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
