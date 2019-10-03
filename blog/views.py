from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Aggregate
import datetime
from .models import *

# Create your views here.
def home(request):
    feature = Post.objects.latest('created_on')
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
