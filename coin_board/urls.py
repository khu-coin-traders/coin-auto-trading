from django.urls import re_path
from coin_board import views


urlpatterns = [


    re_path(r'^$', views.coin_DataBases.get, name = 'coin_databases')
]