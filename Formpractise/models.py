import os.path
import uuid

from django.db import models
def unique_img(instance,filename):
    image = uuid.uuid4()
    ext = filename.split(".")[-1]
    img = f"{image}.{ext}"
    return os.path.join('applications',img)
# Create your models here.
class Student(models.Model):
    choices = ((False,'Male'),(False,'Female'),(False,'Other'))
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    mothers_name = models.CharField(max_length=20,null=True)
    fathers_name = models.CharField(max_length=20,null=True)
    phone_number = models.CharField(unique=True,max_length=30)
    email_address = models.EmailField(unique=True)
    dateofBirth = models.DateField(null=True)
    application = models.ImageField(upload_to=unique_img,default='applications/default.jpg')
    gender = models.BooleanField(choices=choices,default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name
