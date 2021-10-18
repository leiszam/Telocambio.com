from django.db import models
from .user import User
from .product import Product

class Favorite(models.Model):
    favo_id = models.AutoField(primary_key=True)
    favo_user = models.ForeignKey(User, related_name='favo_user', on_delete=models.CASCADE)
    favo_product = models.ForeignKey(Product, related_name='favo_product', on_delete=models.CASCADE)


