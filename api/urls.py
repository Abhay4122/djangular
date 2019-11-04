from django.urls import path
from django.conf.urls import url
# from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^movie/', views.all_movie.as_view()),
]