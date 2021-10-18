from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Acceso no autorizado - Actualización perfil'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().update(request, *args, **kwargs)

