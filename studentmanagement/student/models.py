from django.db import models

# Create your models here.

class Student(models.Model):
    stukdent_id = models.IntegerField().primary_key
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=40)
    department = models.CharField(max_length=40)