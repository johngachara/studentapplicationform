# Generated by Django 4.2.7 on 2023-11-08 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formpractise', '0003_student_fathers_name_student_mothers_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.IntegerField(default=False, unique=True),
        ),
    ]
