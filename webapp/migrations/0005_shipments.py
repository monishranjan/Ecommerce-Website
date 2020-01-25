# Generated by Django 2.0.2 on 2018-04-07 08:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_payments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipments',
            fields=[
                ('shipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('shipment_tracking_number', models.CharField(max_length=15)),
                ('shipment_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('other_shipment_details', models.CharField(max_length=20)),
                ('invoice_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Invoices')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Orders')),
            ],
        ),
    ]
