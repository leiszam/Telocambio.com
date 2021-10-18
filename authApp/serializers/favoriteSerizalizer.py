from authApp.models.user import User
from authApp.models.product import Product
from authApp.models.favorite import Favorite
from rest_framework import serializers


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['favo_user', 'favo_product']

    def to_representation(self, obj): 
        favorite = Favorite.objects.get(favo_id=obj.favo_id)
        product = Product.objects.get(prod_id=obj.favo_product.prod_id)
        user = User.objects.get(id=obj.favo_user.id)

        return {
            "favo_id": favorite.favo_id, 
            "favo_user": {
                "id": user.id,
                "username": user.username,
                "password": user.password,
                "name": user.name,
                "last_name": user.last_name,
                "email": user.email,
                "address": user.address,
                "cellphone": user.cellphone
            }, 
            "favo_product": {
                "prod_id": product.prod_id, 
                "prod_name": product.prod_name, 
                "prod_artist": product.prod_artist, 
                "prod_genre": product.prod_genre, 
                "prod_rate": product.prod_rate, 
                "prod_type": product.prod_type,
                "prod_description": product.prod_description,
                "prod_urlproduct": product.prod_urlproduct,
                "prod_urlimagen": product.prod_urlimagen
            }
        }
