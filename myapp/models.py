from django.db import models


class register_student(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    student_id = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=30,unique=True)

class register_teacher(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    teacher_id = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=30,unique=True)

    

class teacher(models.Model):
    ...

class student(models.Model):
    ...
