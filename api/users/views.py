# -*- coding: utf-8 -*-
"""
api.users.views
~~~~~~~~~~~~~~~

This module implements the logic for user views.

"""
from django.contrib.auth import get_user_model

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import UserSerializer, PasswordSerializer
from .permissions import IsAdminOrSelf

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    To set a password, POST a `password` on the `/set_password/` url.
    """
    permission_classes = (IsAdminOrSelf,)
    model = User
    serializer_class = UserSerializer

    @action()
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.DATA)
        if serializer.is_valid():
            password = self.request.DATA['password']
            if password == '!':
                user.set_unusable_password()
            else:
                user.set_password(password)
                user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
