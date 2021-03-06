# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_auto_20171011_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docsources',
            name='doc_text',
            field=models.CharField(blank=True, max_length=400, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='titlelist',
            name='ready',
            field=models.BooleanField(max_length=1500, verbose_name='Готовность'),
        ),
        migrations.AlterField(
            model_name='titlelist',
            name='title',
            field=models.CharField(default='Title', max_length=200, verbose_name='Название'),
        ),
    ]
