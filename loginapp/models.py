from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80)
class Employee(models.Model):
    eno = models.CharField(max_length=10)
    esal = models.CharField(max_length=10)

