# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('num', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=150)),
                ('handle', models.CharField(max_length=100)),
            ],
        ),
    ]
