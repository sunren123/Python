from django.conf.urls import url

from django.urls import path
from blog import views

urlpatterns = [

    url(r'^index$',views.index),
    url(r'^create$',views.create),
    url(r'^delete(\d+)$',views.delete),
]
