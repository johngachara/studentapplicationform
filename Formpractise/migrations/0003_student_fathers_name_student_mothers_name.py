# Generated by Django 4.2.7 on 2023-11-08 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formpractise', '0002_student_delete_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='fathers_name',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mothers_name',
            field=models.TextField(max_length=20, null=True),
        ),
    ]
