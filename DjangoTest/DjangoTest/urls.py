# from django.conf.urls import url
# # from blog import views
# # urlpatterns = [
# #
# #     url(r'^index$', views.index),
# #     url(r'^create$', views.create),
# #     url(r'^delete(\d+)$', views.delete),
# #
# #
# #     url(r"^login$",views.login),
# #     url(r"^login_check$",views.login_check),
# #     url(r"^change_pwd$",views.change_pwd),
# #     url(r"^change_pwd_action$",views.change_pwd_action),
# #
# # ]
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
