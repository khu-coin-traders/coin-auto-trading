
from django.urls import path, re_path
from coin_main import views

urlpatterns = [
    re_path(r'^$', views.index, name = 'index')
]