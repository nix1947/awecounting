# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-07 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0065_auto_20160706_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='vouchersetting',
            name='enable_purchase_unique_voucher_no',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vouchersetting',
            name='enable_purchase_unique_voucher_no_by_fy',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vouchersetting',
            name='enable_sale_unique_voucher_no',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vouchersetting',
            name='enable_sale_unique_voucher_no_by_fy',
            field=models.BooleanField(default=True),
        ),
    ]
