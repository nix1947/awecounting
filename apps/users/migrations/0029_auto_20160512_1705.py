# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-12 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20160512_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='branch_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Company'),
        ),
    ]
