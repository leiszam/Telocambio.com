from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.favorite import Favorite
from authApp.serializers.favoriteSerizalizer import FavoriteSerializer

class FavoriteDetailView(generics.RetrieveAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Favorite.objects.all()

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Acceso no autorizado - Información detallada de Favorito'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)    

