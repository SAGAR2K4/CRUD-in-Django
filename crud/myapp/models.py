from django.db import models

# Create your models here.
class Member(models.Model) :
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    degree = models.CharField(max_length = 100)
    semester = models.IntegerField()
    division = models.CharField(max_length = 3)
