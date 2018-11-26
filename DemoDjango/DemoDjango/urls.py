


from django.conf.urls import url
from book import views

urlpatterns = [

    url(r'^index$', views.index),
]
