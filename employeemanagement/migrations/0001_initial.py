# Generated by Django 5.0.2 on 2024-03-07 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_id', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('working', models.BooleanField(default=True)),
                ('department', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
