# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-13 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prometapi', '0002_cameras'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='language',
            field=models.TextField(blank=True, null=True),
        ),
    ]