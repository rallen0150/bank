# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0013_transaction_operator3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='num2',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
