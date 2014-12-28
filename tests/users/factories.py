# -*- coding: utf-8 -*-
import factory

from django.utils import timezone
from django.contrib.auth.models import Group

from api.users.models import User


class GroupF(factory.DjangoModelFactory):

    @classmethod
    def _setup_next_sequence(cls):
        try:
            return cls._meta.model._default_manager.values_list(
                'id', flat=True).order_by('-id')[0] + 1
        except IndexError:
            return 0

    name = factory.Sequence(lambda n: "group%s" % n)

    class Meta:
        model = Group


class UserF(factory.DjangoModelFactory):

    @classmethod
    def _setup_next_sequence(cls):
        try:
            return cls._meta.model._default_manager.values_list(
                'id', flat=True).order_by('-id')[0] + 1
        except IndexError:
            return 0

    first_name = factory.Sequence(lambda n: "first_name%s" % n)
    last_name = factory.Sequence(lambda n: "last_name%s" % n)
    email = factory.Sequence(lambda n: "email%s@example.com" % n)
    password = 'sha1$caffc$30d78063d8f2a5725f60bae2aca64e48804272c3'
    is_staff = False
    is_active = True
    is_superuser = False
    last_login = timezone.datetime(2000, 1, 1).replace(tzinfo=timezone.utc)
    password = factory.PostGenerationMethodCall('set_password', 'pass')

    class Meta:
        model = User
