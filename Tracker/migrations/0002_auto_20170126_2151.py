# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-26 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pdesc',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='assign',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='cur_sprint',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='dep_task',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='desc',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='heading',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='remainder',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='risk',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
