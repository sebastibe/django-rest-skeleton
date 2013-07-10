# -*- coding: utf-8 -*-
from rest_framework import routers

from .views import UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls
