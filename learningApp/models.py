from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class AddCourse(models.Model):
    courseid = models.IntegerField()
    coursename = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    trainer = models.CharField(max_length=50)
    sortdesc = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    video  = models.CharField(max_length=500)
    button  = models.CharField(max_length=500)
    fulldesc = models.CharField(max_length=10000)

    def __str__(self):
        return f"{self.courseid} -: {self.coursename}"



class BuyCourse(models.Model):
    username = models.CharField(max_length=50)
    courseids = models.CharField(max_length=1000)
