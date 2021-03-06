# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 02:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20170926_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutcustomer',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2017, 10, 4), null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2017, 10, 4), null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2017, 10, 4), null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='team',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2017, 10, 4), null=True, verbose_name='Дата'),
        ),
    ]
