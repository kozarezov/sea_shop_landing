from django.contrib import admin
from django.urls import path

from . import views
from about.views import about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about', about, name='about'),
]
