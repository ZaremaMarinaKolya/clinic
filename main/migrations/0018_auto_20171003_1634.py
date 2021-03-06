# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20171003_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='banner',
            field=models.ManyToManyField(blank=True, help_text='Задайте, если ваш стиль поддерживает баннеры', null=True, to='banner.BannerPage', verbose_name='Баннер'),
        ),
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.ManyToManyField(blank=True, help_text='Одна или несколько категорий, к которым будет принадлежать страница', null=True, to='main.PageCategory', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='page',
            name='spoiler',
            field=models.ManyToManyField(blank=True, help_text='Задайте, если ваш стиль поддерживает спойлеры', null=True, to='spoiler.SpoilerPage', verbose_name='Спойлер'),
        ),
    ]
