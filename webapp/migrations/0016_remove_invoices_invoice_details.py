# Generated by Django 1.11.12 on 2019-08-24 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_auto_20180410_0659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoices',
            name='invoice_details',
        ),
    ]
