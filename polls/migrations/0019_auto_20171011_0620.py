# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 06:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_titlelist_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ready', models.BooleanField(max_length=1500)),
                ('doc_specification', models.CharField(default='Specification', max_length=500)),
                ('doc_note', models.CharField(blank=True, max_length=400)),
                ('doc_text', models.CharField(default='Text', max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='ok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ready', models.BooleanField(max_length=1500)),
                ('date', models.DateTimeField()),
                ('doc_note', models.CharField(blank=True, max_length=400)),
                ('doc_text', models.CharField(default='Text', max_length=1500)),
            ],
        ),
        migrations.AddField(
            model_name='spisok',
            name='db',
            field=models.URLField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ok',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Spisok'),
        ),
        migrations.AddField(
            model_name='doclist',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Spisok'),
        ),
    ]