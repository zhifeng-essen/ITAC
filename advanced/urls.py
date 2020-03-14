from django.urls import path
from . import views

app_name = 'advanced'

urlpatterns = [
    path('', views.advanced, name='advanced'),
    path('advanced_ajax', views.advanced_ajax, name='advanced_ajax'),
]
