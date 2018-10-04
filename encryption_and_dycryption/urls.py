"""encryption_and_dycryption URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from encryption_and_decryption import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.indexx),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.loginn),
    path('admin/', admin.site.urls),
    path('index/', views.index, name = 'index'),
    path('ceaser/', views.ceaser, name = 'ceaser'),
    path('hill/', views.hill, name = 'hill'),
    path('vernam/', views.vernam, name = 'vernam'),
    path('transportation/', views.transportation, name = 'transportation'),
    path('file/', views.file, name = 'file'),
    path('image/', views.image, name = 'image'),
    path('video/', views.video, name = 'video'),
    path('blog/', views.blog, name = 'blog'),


]
