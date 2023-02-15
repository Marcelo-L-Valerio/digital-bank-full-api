
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    '''Manager for users'''

    def create(self, name, password=None, **extra_fields):
        '''Create, save and return a new user'''

        if 'email' in extra_fields:
            extra_fields['email'] = self.normalize_email(extra_fields['email'])
        elif 'is_admin' in extra_fields:
            extra_fields['email'] = None
            extra_fields.pop('is_admin')
        else:
            raise ValueError('User must have an email address.')

        user = self.model(name=name, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, name, password):
        '''Create and return a new superuser'''
        user = self.create(name, password, is_admin=True)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    '''User registration of basic and personal informations'''

    NATURAL_PERSON = 'PF'
    LEGAL_ENTITY = 'PJ'
    USER_OPTS = [
        (NATURAL_PERSON, 'Fisica'),
        (LEGAL_ENTITY, 'Juridica'),
    ]

    owner_type = models.CharField(max_length=2, choices=USER_OPTS, default='PF')
    cpf = models.CharField(max_length=11, unique=True, null=True)
    cnpj = models.CharField(max_length=14, unique=True, null=True)
    email = models.EmailField(max_length=255, unique=True, null=True)
    name = models.CharField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'name'

    def clean(self):
        '''Validation: an user can't be registered without at least one address'''
        if len(self.address) == 0:
            raise ValidationError('At least one address is required')
        super(User, self).clean()


class Account(models.Model):
    '''Account model, related to an user, witch cotains all
    bancary informations from the user'''

    class Meta:
        unique_together = (('account', 'agency'), )

    CHECKING_ACCOUNT = 'CC'
    SAVINGS_ACCOUNT = 'CP'
    ACCOUNT_OPTS = [
        (CHECKING_ACCOUNT, 'Corrente'),
        (SAVINGS_ACCOUNT, 'Poupanca'),
    ]

    user = models.OneToOneField('user', on_delete=models.CASCADE)
    agency = models.CharField(max_length=5)
    account = models.CharField(max_length=7)
    account_type = models.CharField(max_length=2, choices=ACCOUNT_OPTS, default='CC')
    is_active = models.BooleanField(default=True)
    balance = models.IntegerField(default=0)
    register_date = models.DateField(auto_now_add=True, blank=True)


class Address(models.Model):
    '''Address registration on database'''

    user = models.ForeignKey('user', on_delete=models.CASCADE)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=45)
    district = models.CharField(max_length=45)
    zip_code = models.CharField(max_length=8)
    street = models.CharField(max_length=255)
