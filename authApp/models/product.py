from django.db import models
from .user import User


class Product(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_user= models.ForeignKey(User, related_name='user_producto', on_delete=models.CASCADE)
    prod_name = models.CharField('Name', max_length=30, default=0)
    prod_artist = models.CharField('Artist', max_length=30, default=0)
    prod_genre = models.CharField('Genre', max_length=15, default=0)
    prod_rate = models.BigIntegerField('Rate')
    prod_type = models.CharField('Type', max_length=15, default=0)
    prod_description = models.CharField('Description', max_length=50, default=0)
    prod_urlproduct =models.CharField('imagen', max_length=15, default=0)
    prod_urlimagen =models.CharField('imagen', max_length=15, default=0)
    prod_state =models.BooleanField('State')