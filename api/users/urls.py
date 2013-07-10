# -*- coding: utf-8 -*-
from rest_framework import routers

from .views import UserViewSet, GroupViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = router.urls
