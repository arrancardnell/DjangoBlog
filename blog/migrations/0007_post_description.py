# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170413_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
