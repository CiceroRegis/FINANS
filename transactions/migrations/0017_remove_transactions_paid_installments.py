# Generated by Django 5.0 on 2024-01-25 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0016_transactions_paid_installments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='paid_installments',
        ),
    ]