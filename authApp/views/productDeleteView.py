
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.product import Product
from authApp.serializers.productSerializer import ProductSerializer


class ProductDeteleView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail': 'Acceso no autorizado - Borrar Producto'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        super().destroy(request, *args, **kwargs)
        
        return Response("Producto eliminado", status=status.HTTP_201_CREATED)

