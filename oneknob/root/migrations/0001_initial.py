# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pushed', models.BooleanField(default=False)),
            ],
        ),
    ]
