from django.db import models

# Create your models here.
class Student(models.Model):
    choices = ((False,'Male'),(False,'Female'),(False,'Other'))
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    mothers_name = models.CharField(max_length=20,null=True)
    fathers_name = models.CharField(max_length=20,null=True)
    phone_number = models.CharField(unique=True,max_length=10)
    email_address = models.EmailField(unique=True)
    dateofBirth = models.DateField()
    gender = models.BooleanField(choices=choices,default=False)
    def __str__(self):
        return self.first_name
