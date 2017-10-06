# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutcustomer',
            options={'verbose_name_plural': 'Страница о клиентах'},
        ),
        migrations.AddField(
            model_name='aboutus',
            name='customers',
            field=models.ManyToManyField(to='about.Customers'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='team',
            field=models.ManyToManyField(to='about.Team'),
        ),
    ]