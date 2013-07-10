# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    first_name = serializers.CharField(source='first_name', required=False)
    last_name = serializers.CharField(source='last_name', required=False)
    auth_token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'auth_token', 'groups',
                  'first_name', 'last_name', 'is_staff')


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        widget=forms.PasswordInput(),
        required=False
    )
