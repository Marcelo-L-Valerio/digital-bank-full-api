
from core.models import User, Account, Address
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['user', 'city', 'state', 'district', 'zip_code', 'street', ]


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['user', 'agency', 'account', 'account_type', 'is_active', 'balance', 'register_date', ]


class UserSerializer(serializers.ModelSerializer):

    addresses = AddressSerializer(many=True, required=False, read_only=True)
    accounts = AccountSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'owner_type', 'cpf', 'cnpj', 'email', 'addresses', 'accounts', ]
