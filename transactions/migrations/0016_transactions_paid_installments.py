# Generated by Django 5.0 on 2024-01-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0015_alter_transactions_select'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='paid_installments',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
