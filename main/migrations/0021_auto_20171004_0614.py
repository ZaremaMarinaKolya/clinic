# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 03:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20171004_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='number',
            field=models.IntegerField(blank=True, help_text='Установленное число будет влиять на очерёдность отображения блока', null=True, verbose_name='Порядок'),
        ),
        migrations.AddField(
            model_name='home',
            name='number',
            field=models.IntegerField(blank=True, help_text='Установленное число будет влиять на очерёдность отображения блока', null=True, verbose_name='Порядок'),
        ),
        migrations.AddField(
            model_name='page',
            name='number',
            field=models.IntegerField(blank=True, help_text='Установленное число будет влиять на очерёдность отображения блока', null=True, verbose_name='Порядок'),
        ),
        migrations.AddField(
            model_name='pagecategory',
            name='number',
            field=models.IntegerField(blank=True, help_text='Установленное число будет влиять на очерёдность отображения блока', null=True, verbose_name='Порядок'),
        ),
    ]
