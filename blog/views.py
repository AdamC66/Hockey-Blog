from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Aggregate
import datetime
from .models import *
from .forms import PostForm
from django.utils.text import slugify
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def home(request):
    feature = Post.objects.filter(status=1).latest('created_on')
    recent = Post.objects.filter(status=1).order_by('-id')[:6]
    context={'feature':feature, 'recent':recent}
    return render(request, 'index.html', context)

def article(request, slug):
    post = Post.objects.get(slug=slug)
    context={'post':post}
    return render(request, 'article.html', context)

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'articles.html'

@login_required
def new_post(request):
    if request.method == 'GET':
        context = {'form': PostForm(), 'action': '/newpost/'}
        return render (request, 'newpost.html', context)
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug= slugify(post.title)
            post.save()
            return redirect(article, post.slug)
        else:
            context = {'form':form}
            return render(request, 'newpost.html', context)

@login_required
def edit_post(request, slug):
    post_to_edit = Post.objects.get(slug=slug)
    form = PostForm(request.POST or None, instance = post_to_edit)
    if request.method =='GET':
        context = {'form': form, 'action': f'/edit/{slug}/'}
        return render(request, 'newpost.html', context)
    if request.method=='POST' and form.is_valid():
        form.save()
        return redirect(article, slug)
    else:
        context = {'form': form, 'action': f'/edit/{slug}/'}
        return render(request, 'newpost.html', context)


class all_posts(generic.ListView):
    queryset = Post.objects.filter()
    template_name = 'articles.html'

def delete_post(request, slug):
    post_to_delete = Post.objects.get(slug=slug)
    post_to_delete.delete()
    return redirect('all_posts')
    
    

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                form.add_error('username', 'Login failed')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {
        'form': form
    }) 

