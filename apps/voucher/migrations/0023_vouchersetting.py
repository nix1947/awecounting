# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-06 08:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import njango.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tax', '0005_auto_20160306_1353'),
        ('users', '0021_auto_20160406_1351'),
        ('voucher', '0022_auto_20160330_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoucherSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_voucher_number', models.BooleanField(default=True)),
                ('use_nepali_fy_system', models.BooleanField(default=True)),
                ('single_discount_on_whole_invoice', models.BooleanField(default=True)),
                ('discount_on_each_invoice_particular', models.BooleanField(default=False)),
                ('invoice_default_tax_application_type', models.CharField(blank=True, choices=[('no', 'No Tax'), ('inclusive', 'Tax Inclusive'), ('exclusive', 'Tax Exclusive')], default='inclusive', max_length=10, null=True)),
                ('single_discount_on_whole_purchase', models.BooleanField(default=True)),
                ('discount_on_each_purchase_particular', models.BooleanField(default=False)),
                ('purchase_default_tax_application_type', models.CharField(blank=True, choices=[('no', 'No Tax'), ('inclusive', 'Tax Inclusive'), ('exclusive', 'Tax Exclusive')], default='inclusive', max_length=10, null=True)),
                ('voucher_number_start_date', njango.fields.BSDateField(default=njango.fields.today)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='users.Company')),
                ('invoice_default_tax_scheme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_invoice_tax_scheme', to='tax.TaxScheme')),
                ('purchase_default_tax_scheme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_purchase_tax_scheme', to='tax.TaxScheme')),
            ],
        ),
    ]