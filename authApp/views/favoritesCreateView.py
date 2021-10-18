from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.serializers.favoriteSerizalizer import FavoriteSerializer


class FavoritesCreateView(generics.CreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail':'Acceso no autorizado - Creación de favorito'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        serializer = FavoriteSerializer(data=request.data['favorite_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Favorito creado", status=status.HTTP_201_CREATED)
