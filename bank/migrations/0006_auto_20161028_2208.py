# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='operator1',
            field=models.CharField(choices=[('W', 'Withdraw'), ('D', 'Deposit')], max_length=1),
        ),
    ]
