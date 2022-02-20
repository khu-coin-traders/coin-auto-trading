from django.db import models

import pyupbit
import pybithumb

# 코인 현재 가격 데이터
from . import my_models


class coinCurrentPrice():
    # pybithumb 모듈을 통해 upbit에서 데이터를 불러옴
    tickers = pybithumb.get_tickers()


class myProperty():
    access_key = my_models.access_key
    secret_key = my_models.secret_key

    upbit = pyupbit.Upbit(access_key, secret_key)
    myCoin = upbit.get_balances()
