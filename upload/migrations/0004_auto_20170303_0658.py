# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 06:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_new_second_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new_second_data',
            old_name='N_Class',
            new_name='Class',
        ),
        migrations.RenameField(
            model_name='new_second_data',
            old_name='N_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='new_second_data',
            old_name='N_handle',
            new_name='handle',
        ),
        migrations.RenameField(
            model_name='new_second_data',
            old_name='N_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='new_second_data',
            old_name='N_num',
            new_name='num',
        ),
    ]
