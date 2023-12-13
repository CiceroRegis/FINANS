# Generated by Django 4.1 on 2023-02-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks_accounts', '0004_rename_default_accounts_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=10, verbose_name='Saldo Bancário'),
        ),
    ]