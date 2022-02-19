from django.http import HttpResponse
from django.shortcuts import render

from coin_main.models import coinCurrentPrice

# request는 항상 맨 첫번째 인수로 오게끔
def index(request) :
    template_name = 'coin_main/index.html'
    
    # 코인 현재 가격 데이터
    coin_current_price = coinCurrentPrice.tickers

    # render = 화면에 html파일 띄워주는 함수 (request와 html파일주소 필수)
    # 필요 변수는 튜플로 묶어서 보냄
    return render(request, template_name, {"coin_current_price":coin_current_price})

