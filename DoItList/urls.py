"""DoItList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from django.contrib import admin

from django.conf.urls import url, include
from django.shortcuts import redirect

from . import views

urlpatterns = [
    url(r'todo/', include('todo.urls', namespace='todo')),
    url(r'login/', views.user_login, name='login'),
    url(r'logout/', views.logout, name='logout'),
    url(r'register/', views.register, name='register'),
    url(r'^', views.user_login, name='home'),
    # Wanted to redirect '/' to login url but runs into circular import issues?
    # Not worth digging in now, I'll just render the same view
]
