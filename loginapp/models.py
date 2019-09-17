from django.db import models


class Person(models.Model):
    User_name = models.CharField(max_length=10)
    Password = models.CharField(max_length=10)


    class Meta:
        db_table = "Person"
