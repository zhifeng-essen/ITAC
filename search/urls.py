from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.search, name='search'),
    path('search_ajax', views.search_ajax, name='search_ajax'),
    path('search_th', views.search_th, name='search_th'),
]
