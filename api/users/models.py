# -*- coding: utf-8 -*-

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# every user to have an automatically generated Token
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
