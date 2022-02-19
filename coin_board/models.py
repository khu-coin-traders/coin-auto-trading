from django.db import models

# Create your models here.

class CoinDb(models.Model):
    name = models.CharField(max_length=10)
    id = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'coin_db'
