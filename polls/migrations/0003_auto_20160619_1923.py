# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-19 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160619_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.Poll'),
        ),
    ]
