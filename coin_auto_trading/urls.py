"""coin_auto_trading URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path, include

# localhost 접속 후 맨처음 들어오는 곳
urlpatterns = [
    # 주소에 따라 목적지 설정
    path('admin/', admin.site.urls), # 관리자 페이지
    path('', include('coin_main.urls')), # 메인화면 페이지
    path('board/', include('coin_board.urls'), name = 'board'), # databases 페이지
]
