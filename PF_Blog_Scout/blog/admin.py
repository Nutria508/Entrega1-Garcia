from django.contrib import admin

# Register your models here.
from blog.models import Request,Blog,Avatar

admin.site.register(Request)

admin.site.register(Blog)

admin.site.register(Avatar)
