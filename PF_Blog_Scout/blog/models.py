
from cgitb import text
from django.db import models
from django .contrib.auth.models import User

# Create your models here.


class Blog (models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    text = models.CharField(max_length=120)
    post_date = models.DateField()
    image1= models.ImageField(upload_to='blogs',null=True,blank=True)
    image2= models.ImageField(upload_to='blogs',null=True,blank=True)
    def __str__(self):
        return f"Autor: {self.autor} - Titulo: {self.title} - Fecha: {self.post_date} "

class Request (models.Model):
    
    date = models.DateField()
    text = models.CharField(max_length=50)
    votes = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.text} - fecha {self.date} - votos {self.votes} "


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='avatars',null=True,blank=True)