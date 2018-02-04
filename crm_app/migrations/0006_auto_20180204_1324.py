# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-04 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0005_auto_20180203_0646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='status',
        ),
        migrations.AddField(
            model_name='project',
            name='project_status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Active'), (2, 'Inactive'), (3, 'Complete')], default=0),
            preserve_default=False,
        ),
    ]
