from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from about.views import about
from news.views import news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about', about, name='about'),
    path('news/<int:pk>/', news, name='news'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

handler404 = 'sea_shop.views.error_404_view'
handler500 = 'sea_shop.views.error_500_view'
handler403 = 'sea_shop.views.error_403_view'
