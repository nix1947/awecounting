# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-06 07:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0064_auto_20160705_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditvoucherrow',
            name='cash_payment',
        ),
        migrations.RemoveField(
            model_name='debitvoucherrow',
            name='cash_receipt',
        ),
    ]
