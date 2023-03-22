"""mysite_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# Replaces the standard django.urls.path, identical syntax
#from django_distill import distill_path

# Import some views from your Django app
#from catalog.views import index

#urlpatterns = [
#
#    # The index URL on /, render this as 'index.html'
#    distill_path('',
#                'admin/', admin.site.urls)
#
#    # A single static page, render this as 'page.html'
#    distill_path('home.html',
#                index.as_view(),
#                name='page')
#
#]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('catalog.urls')),          #home page
    path('polls/', include('polls.urls')),      #sub page
    path('admin/', admin.site.urls)             #admin portal
]
