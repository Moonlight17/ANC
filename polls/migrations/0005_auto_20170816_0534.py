# Generated by Django 2.0.dev20170814182805 on 2017-08-16 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170815_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spisok',
            name='doc_text',
        ),
        migrations.RemoveField(
            model_name='spisok',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='spisok',
            name='doc_note',
            field=models.CharField(default='Note', max_length=400),
        ),
        migrations.AddField(
            model_name='spisok',
            name='doc_specification',
            field=models.CharField(default='Specification', max_length=1500),
        ),
        migrations.AlterField(
            model_name='spisok',
            name='doc_title',
            field=models.CharField(default='Title', max_length=200),
        ),
    ]