# Generated by Django 2.0.2 on 2018-04-07 08:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('invoice_number', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('invoice_details', models.CharField(max_length=20)),
                ('invoice_status_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Ref_Invoice_Status_Codes')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Orders')),
            ],
        ),
    ]
