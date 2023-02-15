
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import viewsets


router = DefaultRouter()
router.register('user', viewsets.UserViewset)
router.register('account', viewsets.AccountViewset)
router.register('address', viewsets.AddressViewset)

app_name = 'user'

urlpatterns = [
    path('', include(router.urls)),
]