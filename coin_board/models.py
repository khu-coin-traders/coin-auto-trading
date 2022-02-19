from django.db import models

# Create your models here.

# mysql 데이터베이스 설정

# py manage.py inspectdb 명령어를 통해 나온 db 내용 복붙
class CoinDb(models.Model):
    name = models.CharField(max_length=10)
    id = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'coin_db'
