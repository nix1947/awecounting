# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 13:29
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0006_auto_20160523_1709'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
