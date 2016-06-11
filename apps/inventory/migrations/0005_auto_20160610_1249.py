# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 07:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationContain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Item')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='contains',
            field=models.ManyToManyField(to='inventory.LocationContain'),
        ),
    ]