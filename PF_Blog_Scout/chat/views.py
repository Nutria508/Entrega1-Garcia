from django.urls import reverse
from chat.models import Messages
from blog.models import Blog
from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
def message_forms_django(request, pk:int):
    #print(request.__dict__)
    if request.GET['body']:
        blog_id=pk
        
        new_message = Messages(
            blog=Blog.objects.get(pk=blog_id),
            body=request.GET['body'],
            post_date=datetime.today().strftime('%Y-%m-%d'),
            author=request.user,
        ) 
        new_message.save()
        return redirect(f"/pages/blog/{blog_id}/detail")




def new_message(body:str,blog_id:int,user_id:int):
    new_message = Messages(
            blog=blog_id,
            body=body,
            post_date=datetime.today().strftime('%Y-%m-%d'),
            author=user_id,
        )
    new_message.save()
    return



def all_message(id):
    all_messages=Messages.objects.all()
    for message in all_messages:
        if message.blog==id:
            view_message=message.add