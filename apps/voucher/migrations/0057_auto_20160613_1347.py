# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0056_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='lot_number',
            field=models.CharField(default=None, max_length=150, unique=True),
            preserve_default=False,
        ),
    ]