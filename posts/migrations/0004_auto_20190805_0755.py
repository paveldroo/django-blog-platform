# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-08-05 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0003_auto_20190801_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(blank=True),
        ),
    ]