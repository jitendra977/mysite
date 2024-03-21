# Generated by Django 5.0.2 on 2024-03-21 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monthlybudget', '0005_alter_transactions_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='payment_method',
            field=models.CharField(choices=[('PayPay', 'PayPay'), ('Cash', 'Cash'), ('Credit', 'Credit'), ('E-money', 'E-money'), ('Bank', 'Bank')], max_length=50),
        ),
    ]
