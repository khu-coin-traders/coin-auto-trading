
from django.shortcuts import render
from django.views import generic

from coin_board.models import CoinDb


class coin_DataBases(generic.TemplateView):
    # request는 항상 함수의 첫번째 파라미터로 입력해야함
    # self 가 첫번째 인자로 들어가면 에러뜸!
    def get(request, *args, **kwargs):
        template_name = 'coin_board/UserData.html'
        coin_db = CoinDb.objects.all()

        # render(request, 템플릿주소, {"템플릿에서 쓸 이름":데이터베이스.objects.all()}
        return render(request, template_name, {"coin_db" : coin_db})