"""hockeyblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.PostList.as_view(), name='posts'),
    path('posts/<slug:slug>/', views.article, name='article'),
    path('newpost/', views.new_post, name='new_post'),
    path('allposts', login_required(views.all_posts.as_view()), name='all_posts'),
    path('edit/<slug:slug>/', views.edit_post, name="edit_post"),
    path('delete/<slug:slug>/', views.delete_post, name="delete_post"),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': 'views.home'}, name='logout'),
]
