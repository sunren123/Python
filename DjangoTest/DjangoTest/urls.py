from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^create$', views.create),
    url(r'^delete(\d+)$', views.delete),


    url(r"^login$",views.login),
    url(r"^login_check$",views.login_check),
    url(r"^get_session$",views.get_session),
    url(r"^set_session$",views.set_session),

]
