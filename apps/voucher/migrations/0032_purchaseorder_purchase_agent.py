# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-15 06:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voucher', '0031_auto_20160506_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='purchase_agent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='purchase_order', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
