"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("",views.home,name='home'),
     path("index",views.home,name='home'),
     path("sign",views.signup,name='signup'),
     path("mentee_reg",views.mentee_reg,name='mentee_reg'),
     path("mentor_reg",views.mentor_reg,name='mentor_reg'),
     path("about",views.about,name='index'),
     path("blog",views.blog,name='index'),
     path("blog_details",views.blog_details,name='blog_details'),
     path("contact",views.contact,name='contact'),
     path("projects",views.projects,name='projects'),
     path("projects_details",views.projects_details,name='projects_details'),
     path("services",views.services,name='services')
]
