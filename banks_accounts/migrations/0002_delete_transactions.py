# Generated by Django 4.1 on 2023-01-31 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banks_accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transactions',
        ),
    ]