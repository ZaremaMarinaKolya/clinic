# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 22:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170929_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2017, 10, 2), null=True, verbose_name='Дата'),
        ),
    ]
