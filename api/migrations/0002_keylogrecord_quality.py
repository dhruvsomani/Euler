# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-23 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='keylogrecord',
            name='quality',
            field=models.CharField(default='white', max_length=8),
        ),
    ]
