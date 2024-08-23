from django.db import models

class com_sub(models.Model):
    math=models.IntegerField()
    english=models.IntegerField()
    science=models.IntegerField()
    social=models.IntegerField()
    nepali=models.IntegerField()

class basic_level(com_sub):
    sub6=models.IntegerField()
    sub7=models.IntegerField()


class secondary_level(com_sub):
    sec1=models.IntegerField()
    sec2 = models.IntegerField()

