
from django.urls import path, re_path
from coin_main import views

urlpatterns = [
    # path 아닌 re_path 사용 (url과 같은 역할)
    # 다시 목적지 설정
    re_path(r'^$', views.index, name = 'index'),
    re_path(r'^mydata$', views.myCoinData, name = 'myData'),

    # 현재가 검색창 부분
    #re_path(r'^search$', views.SearchFormView.as_view(), name = 'search')
]