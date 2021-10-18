from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.serializers.exchangeSerizalizer import ExchangeSerializer
from authApp.models.product import Product

class ExchangeCreateView(generics.CreateAPIView):
    serializer_class = ExchangeSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail':'Acceso no autorizado - Creación de Intercambio'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        serializer = ExchangeSerializer(data=request.data['exchange_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        datos = request.data['exchange_data']
        id_user_origin =datos["exch_userorigin"]
        id_user_destination = datos['exch_userdestination']
        id_product = datos['exch_prod']
        Product.objects.filter(prod_user=id_user_origin).filter(prod_id=id_product).update(prod_user = id_user_destination)
        
        return Response("Intercambio creado", status=status.HTTP_201_CREATED)

