# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_remove_titlelist_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='titlelist',
            name='upload',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='images/blog/%Y/%m/%d', verbose_name='Документ'),
        ),
    ]
