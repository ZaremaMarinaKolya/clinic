# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 01:23
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0004_auto_20171002_0421'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите заголовок страницы', max_length=250, null=True)),
                ('descriptions', models.TextField(blank=True, help_text='Введите описание для поисковых систем', max_length=1000, null=True)),
                ('keywords', models.TextField(blank=True, help_text='Введите ключевые слова для поисковых систем', max_length=1000, null=True)),
                ('slug', models.SlugField(help_text='Slug влияет на формирование url адреса и должен быть уникальным', null=True, unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Содержание страницы')),
                ('date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, help_text='Выберите изображение баннера', null=True, upload_to='', verbose_name='Изображение')),
                ('name', models.CharField(default='Баннер', max_length=250, verbose_name='Заголовок баннера')),
                ('brief', models.CharField(blank=True, help_text='Не более 500 знаков', max_length=500, null=True, verbose_name='Краткий лозунг')),
                ('url', models.URLField(blank=True, help_text='Вставьте URL-адрес', max_length=500, null=True, verbose_name='URL-адрес баннера')),
            ],
            options={
                'verbose_name_plural': 'Баннер 3',
            },
        ),
    ]
