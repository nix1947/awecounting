# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 10:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20160610_1516'),
        ('voucher', '0049_sale_from_locations'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleFromLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Location')),
                ('sale_row', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voucher.SaleRow')),
            ],
        ),
        migrations.RemoveField(
            model_name='sale',
            name='from_locations',
        ),
        migrations.AlterUniqueTogether(
            name='salefromlocation',
            unique_together=set([('sale_row', 'location')]),
        ),
    ]
