# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spoiler', '0003_auto_20171002_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spoiler1',
            name='name',
            field=models.CharField(default='Spoiler', max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='spoiler2',
            name='name',
            field=models.CharField(default='Spoiler', max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='spoiler3',
            name='name',
            field=models.CharField(default='Spoiler', max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='spoilerpage',
            name='name',
            field=models.CharField(default='Spoiler', max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='spoilerpagebanner',
            name='name',
            field=models.CharField(default='Spoiler', max_length=250, verbose_name='Название'),
        ),
    ]
