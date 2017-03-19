# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-18 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0007_auto_20170315_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtask',
            name='task',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='project',
            new_name='tproject',
        ),
        migrations.RemoveField(
            model_name='sprint',
            name='task',
        ),
        migrations.AddField(
            model_name='member',
            name='mgroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tracker.group'),
        ),
        migrations.AddField(
            model_name='sprint',
            name='status',
            field=models.CharField(default='Green', max_length=10, verbose_name='Sprint Status'),
        ),
        migrations.AddField(
            model_name='task',
            name='tsprint',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tracker.sprint'),
        ),
        migrations.DeleteModel(
            name='subtask',
        ),
    ]
