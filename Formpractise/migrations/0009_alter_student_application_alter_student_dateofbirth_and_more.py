# Generated by Django 4.2.7 on 2023-11-11 07:22

import Formpractise.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formpractise', '0008_student_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='application',
            field=models.ImageField(default='employees/default.jpg', upload_to=Formpractise.models.unique_img),
        ),
        migrations.AlterField(
            model_name='student',
            name='dateofBirth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
