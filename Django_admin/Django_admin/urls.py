"""Django_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login$',views.login),
    url(r'^login_check$',views.login_check),
    url(r'^index$',views.index),

    url(r'^classes$',views.classes),
    url(r'^add_classes$',views.add_classes),
    url(r'^del_classes$',views.del_classes),
    url(r'^edit_classes$',views.edit_classes),


    url(r'^students$',views.get_students),
    url(r'^add_students$',views.add_students),


    url(r'^ajax1$',views.ajax1),
    url(r'^ajax2$',views.ajax2),
    url(r'^ajax3$',views.ajax3),


]
