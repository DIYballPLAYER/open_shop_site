from django.urls import path

from core.views import home, phones, page3

urlpatterns = [
    path('', home, name='home'),
    path('phones/', phones, name='phones'),
    path('smthing/', page3, name='smthing')
]

