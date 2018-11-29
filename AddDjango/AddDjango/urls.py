
from django.conf.urls import include, url
from django.contrib import admin
from blog import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^show_upload$', views.show_upload),
    url(r'^show_area(?P<pindex>\d*)$', views.show_area),
    url(r'^areas$', views.areas),
]
