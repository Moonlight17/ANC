# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 09:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_auto_20171025_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spisok',
            name='db',
        ),
        migrations.RemoveField(
            model_name='spisok',
            name='doc_TXT',
        ),
        migrations.RemoveField(
            model_name='spisok',
            name='doc_specification',
        ),
        migrations.RemoveField(
            model_name='spisok',
            name='doc_text',
        ),
        migrations.AddField(
            model_name='spisok',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='docsources',
            name='doc_text',
            field=models.TextField(max_length=400, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='titlelist',
            name='doc_note',
            field=models.CharField(max_length=400, verbose_name='Заметка'),
        ),
        migrations.AlterField(
            model_name='titlelist',
            name='doc_specification',
            field=models.CharField(max_length=500, verbose_name='Спецификация'),
        ),
        migrations.AlterField(
            model_name='titlelist',
            name='doc_text',
            field=models.TextField(max_length=1500, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='titlelist',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='titlelist',
            name='upload',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='images/blog/%Y/%m/%d', verbose_name='Изображение'),
        ),
    ]
