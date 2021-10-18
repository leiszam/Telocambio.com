from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.product import Product
from authApp.serializers.productSerializer import ProductSerializer

class ProductUserListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Acceso no autorizado - Lista de elementos'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Product.objects.filter(prod_user_id=self.kwargs['user'])

        return queryset


