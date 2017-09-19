# Generated by Django 2.0.dev20170814182805 on 2017-09-18 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20170914_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='TitleList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_ready', models.BooleanField(max_length=1500)),
                ('doc_TXT', models.BooleanField(max_length=1500)),
                ('doc_title', models.CharField(default='Title', max_length=200)),
                ('doc_specification', models.CharField(default='Specification', max_length=500)),
                ('doc_note', models.CharField(blank=True, max_length=400)),
                ('doc_text', models.CharField(default='Text', max_length=1500)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Spisok')),
            ],
        ),
    ]