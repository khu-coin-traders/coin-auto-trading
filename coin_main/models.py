from django.db import models


import pybithumb

# 코인 현재 가격 데이터
class coinCurrentPrice():
    # pybithumb 모듈을 통해 upbit에서 데이터를 불러옴
    tickers = pybithumb.get_tickers()


