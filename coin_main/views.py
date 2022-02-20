from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView

from coin_main.forms import presentPriceSearch
from coin_main.models import coinCurrentPrice, myProperty


# request는 항상 맨 첫번째 인수로 오게끔
def index(request) :
    template_name = 'coin_main/index.html'
    
    # 코인 티커 데이터
    coin_current_price = coinCurrentPrice.tickers

    # render = 화면에 html파일 띄워주는 함수 (request와 html파일주소 필수)
    # 필요 변수는 튜플로 묶어서 보냄
    return render(request, template_name, {"coin_current_price":coin_current_price})

def myCoinData(request):
    template_name = 'coin_main/myCoinData.html'
    my_coin = myProperty.myCoin
    return render(request, template_name, {"my_coin":my_coin})

'''
# 현재가 검색 view
class SearchFormView(FormView):
    form_class = presentPriceSearch
    template_name = 'coin_main/price_search.html'
'''
