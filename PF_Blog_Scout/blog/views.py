from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict

from blog.models import Blog, User, Request
from blog.forms import BlogForm,UserForm,RequestForm
# Create your views here.


def index(request):
    return render(request, "blog/home.html")



##    Blogs

def blogs(request):
    blog = Blog.objects.all()

    context_dict = {
        'blogs': blog
    }

    return render(
        request=request,
        context=context_dict,
        template_name="blog/blogs.html"
    )


def blog_forms_django(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            data = blog_form.cleaned_data
            blog = Blog(
                title=data['title'],
                subtitle=data['subtitle'],
                autor=data['autor'],
                text=data['text'],
                post_date=data['post_date'],
                )
            blog.save()

            blogs = Blog.objects.all()
            context_dict = {
                'blogs': blogs
            }
            return render(
                request=request,
                context=context_dict,
                template_name="blog/blogs.html"
            )

    blog_form = BlogForm(request.POST)
    context_dict = {
        'blog_form': blog_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog/blog_forms.html'
    )


##    Request

def request(request):
    requests = Request.objects.all()

    context_dict = {
        'requests': requests
    }

    return render(
        request=request,
        context=context_dict,
        template_name="blog/request.html"
    )




def request_forms_django(request):
    if request.method == 'POST':
        request_form = RequestForm(request.POST)
        if request_form.is_valid():
            data = request_form.cleaned_data
            new_request = Request(
                text=data['text'],
                date=data['date'],
                )
            new_request.save()

            requests = Request.objects.all()
            context_dict = {
                'requests': requests
            }
            return render(
                request=request,
                context=context_dict,
                template_name="blog/request.html"
            )

    request_form = RequestForm(request.POST)
    context_dict = {
        'request_form': request_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog/request_forms.html'
    )



##    USERS

def users(request):
    users = User.objects.all()

    context_dict = {
        'users': users
    }

    return render(
        request=request,
        context=context_dict,
        template_name="blog/users.html"
    )



def user_forms_django(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            data = user_form.cleaned_data
            new_user = User(
                name=data['name'],
                last_name=data['last_name'],
                email=data['email'],
                password=data['password'],
                )
            new_user.save()

            users = Blog.objects.all()
            context_dict = {
                'users': users
            }
            return render(
                request=request,
                context=context_dict,
                template_name="blog/users.html"
            )

    user_form = UserForm(request.POST)
    context_dict = {
        'user_form': user_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog/user_form.html'
    )


def search(request):
    context_dict = dict()
    if request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(title__contains=search_param)
        query.add(Q(subtitle__contains=search_param), Q.OR)
        query.add(Q(autor__contains=search_param), Q.OR)
        blogs = Blog.objects.filter(query)
        context_dict = {
            'blogs': blogs
        }
    return render(
    request=request,
    context=context_dict,
    template_name="blog/blogs.html",
    )