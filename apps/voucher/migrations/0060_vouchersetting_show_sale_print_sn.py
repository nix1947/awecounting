# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-14 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0059_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='vouchersetting',
            name='show_sale_print_sn',
            field=models.BooleanField(default=True),
        ),
    ]