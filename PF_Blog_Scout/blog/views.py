from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import datetime

from blog.models import Blog, Request
from chat.models import Messages


#BLOG


class blogs(ListView):
    
    model = Blog
    template_name = "blog/blog_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_objects"]=True
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_single.html"
    fields = ['title', 'subtitle', 'author', 'text', 'post_date','image']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = context['blog']
        blog_id=blog.id
        messages=Messages.objects.filter(blog=blog_id)
        count=len(messages)
        context["message_list"]=messages
        context["count"]=count
        return context


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    success_url = reverse_lazy('blog:Blogs')
    fields = ['title', 'subtitle', 'text','image']

    def form_valid(self, form):
        form.instance.author= self.request.user
        form.instance.post_date=datetime.today().strftime('%Y-%m-%d')
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    success_url = reverse_lazy('blog:Blogs')
    fields = ['title', 'subtitle', 'text']


class BlogUpdateImage(PermissionRequiredMixin, UpdateView):
    permission_required = 'user.delete_user'
    model = Blog
    success_url = reverse_lazy('blog:Blogs')
    fields = ['image']


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:Blogs')


#REQUEST


class request(ListView):

    model = Request
    template_name = "blog/request_list.html"


class RequestCreateView(LoginRequiredMixin, CreateView):
    model = Request
    success_url = reverse_lazy('blog:Request')
    fields = ['text']

    def form_valid(self, form):
        form.instance.votes=1
        form.instance.date=datetime.today().strftime('%Y-%m-%d')
        return super().form_valid(form)

class RequestUpdateView(LoginRequiredMixin, UpdateView):
    model = Request
    success_url = reverse_lazy('blog:Request')
    fields = ['text']


class RequestDeleteView(LoginRequiredMixin, DeleteView):
    model = Request
    success_url = reverse_lazy('blog:Request')

@login_required
def vote_request(request, pk: int):
    request1 = Request.objects.get(pk=pk)
    if request1 is not None:
        request1.votes += 1
        request1.save()
        return redirect("blog:Request")

#SEARCH


def search(request):
    context_dict = dict()
    try:
        if request.GET['all_search']:
            search_param = request.GET['all_search']
            query = Q(title__contains=search_param)
            query.add(Q(subtitle__contains=search_param), Q.OR)
            #query.add(Q(author__contains=search_param), Q.OR)
            blogs = Blog.objects.filter(query)
            context_dict = {
                'blog_list': blogs,
                'all_objects' : False
            }
    except:
        if request.GET['author_search']:
            user_id = request.GET['author_search']
            blogs = Blog.objects.filter(author=user_id)
            context_dict = {
                'blog_list': blogs,
                'all_objects' : False
            }

    return render(
    request=request,
    context=context_dict,
    template_name="blog/blog_list.html",
    )



