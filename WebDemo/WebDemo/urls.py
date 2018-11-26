
from django.conf.urls import url

from Web import views

urlpatterns = [



    url(r'^set_cookie$', views.set_cookie),
    url(r'^get_cookie$', views.get_cookie),


]
