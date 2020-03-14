from django.urls import path
from . import views

app_name = 'rambler'

urlpatterns = [
    path('', views.index, name='index'),
    path('browse', views.browse, name='browse'),
    path('browse_ajax', views.browse_ajax, name='browse_ajax'),
    path('detail/<str:ID>/', views.detail, name='detail'),
    path('detail_ajax', views.detail_ajax, name='detail_ajax'),
]
