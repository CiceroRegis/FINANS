# Generated by Django 4.1 on 2023-01-31 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_alter_transactions_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Valor'),
        ),
    ]
