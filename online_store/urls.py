from django.conf import settings
from django.urls import path

from core.views import home

urlpatterns = [
    path('', home, name='home_page')
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL)
