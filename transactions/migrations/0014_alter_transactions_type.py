# Generated by Django 4.1.6 on 2023-03-22 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0013_remove_transactions_date_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='type',
            field=models.CharField(choices=[('', '---------'), ('Receitas', 'Receitas'), ('Despesas', 'Despesas')], default='', max_length=10, verbose_name='Despesas e Receita'),
        ),
    ]
