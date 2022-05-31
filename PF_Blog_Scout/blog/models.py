
from cgitb import text
from django.db import models

# Create your models here.


class Blog (models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    text = models.CharField(max_length=120)
    post_date = models.DateField()



class User (models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)



class Request (models.Model):
    date = models.DateField()
    text = models.CharField(max_length=50)



