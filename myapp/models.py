from django.db import models


class register_user(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10)
    person_id = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=30,unique=True)
    

class teacher(models.Model):
    ...

class student(models.Model):
    ...
