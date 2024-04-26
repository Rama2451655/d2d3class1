from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.IntegerField(unique=True,null=True)
    age=models.IntegerField(null=True)
    email=models.CharField(max_length=50,unique=True,null=True)
