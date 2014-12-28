# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    auth_token = serializers.CharField(read_only=True)
    last_login_at = serializers.DateTimeField(source='last_login', read_only=True)
    joined_at = serializers.DateTimeField(source='date_joined', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'auth_token', 'first_name',
                  'last_name', 'is_staff', 'last_login_at',
                  'joined_at')


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        style={'type': 'password'},
        required=False
    )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    permissions = serializers.SlugRelatedField(
        many=True,
        required=False,
        slug_field='codename',
        queryset=Permission.objects.all()
    )

    class Meta:
        model = Group
        fields = ('url', 'name', 'permissions')
