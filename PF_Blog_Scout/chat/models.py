from django.db import models
from django .contrib.auth.models import User
from blog.models import Blog
# Create your models here.

class Messages (models.Model):
    body = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
    post_date = models.DateField()