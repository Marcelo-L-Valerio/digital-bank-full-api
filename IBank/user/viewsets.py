
from .serializers import UserSerializer, AddressSerializer, AccountSerializer
from rest_framework import viewsets
from core.models import User, Account, Address


class UserViewset(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class AddressViewset(viewsets.ModelViewSet):

    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class AccountViewset(viewsets.ModelViewSet):

    serializer_class = AccountSerializer
    queryset = Account.objects.all()