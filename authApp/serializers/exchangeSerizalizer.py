from authApp.models.user import User
from authApp.models.product import Product
from authApp.models.exchange import Exchange
from rest_framework import serializers

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = ['exch_userorigin', 'exch_userdestination', 'exch_prod', 'exch_fecha']

    def to_representation(self, obj):
        product = Product.objects.get(prod_id=obj.exch_prod.prod_id)
        userorigin = User.objects.get(id=obj.exch_userorigin.id)
        userdestination = User.objects.get(id=obj.exch_userdestination.id)
        exchange = Exchange.objects.get(exch_id=obj.exch_id)

        return {
            "exch_id" : exchange.exch_id, 
            "exch_fecha" : exchange.exch_fecha,
            "exch_userorigin" : {
                "id": userorigin.id,
                "username": userorigin.username,
                "name": userorigin.name,
                "last_name": userorigin.last_name,
                "email": userorigin.email,
                "address": userorigin.address,
                "cellphone": userorigin.cellphone
            },
            "exch_userdestination" : {
                "id": userdestination.id,
                "username": userdestination.username,
                "name": userdestination.name,
                "last_name": userdestination.last_name,
                "email": userdestination.email,
                "address": userdestination.address,
                "cellphone": userdestination.cellphone
            },
            "exch_prod" : {
                "prod_id": product.prod_id, 
                "prod_name": product.prod_name, 
                "prod_artist": product.prod_artist, 
                "prod_genre": product.prod_genre, 
                "prod_rate": product.prod_rate, 
                "prod_type": product.prod_type,
                "prod_description": product.prod_description,
                "prod_urlproduct": product.prod_urlproduct,
                "prod_urlimagen": product.prod_urlimagen,
            }
        }




        