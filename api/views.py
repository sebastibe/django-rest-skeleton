# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser


@api_view(['GET'])
@permission_classes([IsAdminUser, ])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({'Welcome': 'Home!'})
