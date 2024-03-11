# Generated by Django 5.0.2 on 2024-03-11 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeemanagement', '0002_rename_emp_id_employee_employee_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('testimonial', models.TextField()),
                ('picture', models.ImageField(upload_to='testimonials/')),
                ('rating', models.ImageField(max_length=1, upload_to='')),
            ],
        ),
    ]
