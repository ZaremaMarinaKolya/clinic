# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 01:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_home_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2017, 9, 26), null=True, verbose_name='Дата'),
        ),
    ]
