# Generated by Django 5.0.2 on 2024-03-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('Personal', 'Personal'), ('Food', 'Food'), ('Health', 'Health'), ('Transportation', 'Transportation'), ('Clothes', 'Clothes')], max_length=50)),
                ('payment_method', models.CharField(choices=[('PayPal', 'PayPal'), ('Credit', 'Credit'), ('Cash', 'Cash'), ('Copen', 'Copen')], max_length=50)),
            ],
        ),
    ]
