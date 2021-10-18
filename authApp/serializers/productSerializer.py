from authApp.models.user import User
from authApp.models.product import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['prod_user', 'prod_name', 'prod_artist', 'prod_genre', 'prod_rate', 'prod_type', 'prod_description', 'prod_urlproduct', 'prod_urlimagen', 'prod_state']

    def to_representation(self, obj):
        
        product = Product.objects.get(prod_id=obj.prod_id)
        user = User.objects.get(id=obj.prod_user.id)

        return {
            "prod_id": product.prod_id, 
            "prod_name": product.prod_name, 
            "prod_artist": product.prod_artist, 
            "prod_genre": product.prod_genre, 
            "prod_rate": product.prod_rate, 
            "prod_type": product.prod_type,
            "prod_description": product.prod_description,
            "prod_urlproduct": product.prod_urlproduct,
            "prod_urlimagen": product.prod_urlimagen,
            "prod_state": product.prod_state,
            "prod_user": {
                "id": user.id,
                "username": user.username,
                "password": user.password,
                "name": user.name,
                "last_name": user.last_name,
                "email": user.email,
                "address": user.address,
                "cellphone": user.cellphone
            }
        }
        