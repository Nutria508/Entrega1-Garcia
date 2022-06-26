
from cgitb import text
from django.db import models
from ckeditor.fields import RichTextField
from django .contrib.auth.models import User

# Create your models here.


class Blog (models.Model):
    title = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=60)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #text = models.TextField(blank=True, null=True)
    text=RichTextField(blank=True, null=True)
    post_date = models.DateField()
    image= models.ImageField(upload_to='pages/',null=True,blank=True)
    def __str__(self):
        return f"Autor: {self.author} - Titulo: {self.title} - Fecha: {self.post_date} "

class Request (models.Model):
    
    date = models.DateField()
    text = models.CharField(max_length=50)
    votes = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.text} - fecha {self.date} - votos {self.votes} "


