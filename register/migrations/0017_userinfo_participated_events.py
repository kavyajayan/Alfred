# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-22 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0016_userinfo_printed'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='participated_events',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]