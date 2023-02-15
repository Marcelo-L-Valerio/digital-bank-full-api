
from django.test import TestCase
from core.models import User, Account, Address


def create_user(cpf='12345678910', email='test@example.com',
                name='TestUser', password='Testpass123'):
    '''Assist function for agile user creation'''
    return User.objects.create(cpf=cpf, email=email, name=name, password=password)


class UserAppTests(TestCase):

    def test_create_user(self):

        payload = {
            'cpf': '12345678910',
            'email': 'test@example.com',
            'name': 'TestUser',
        }
        password = 'Testpass123'
        user = User.objects.create(**payload, password=password)

        for param, value in payload.items():
            self.assertEqual(getattr(user, param), value)
        self.assertTrue(user.check_password(password))

    def test_normalize_email(self):

        payload = {
            'cpf': '12345678910',
            'email': 'TEst@ExampLE.cOM',
            'name': 'TestUser',
        }
        password = 'Testpass123'
        user = User.objects.create(**payload, password=password)

        self.assertEqual(user.email, 'TEst@example.com')

    def test_create_super_user(self):

        user = User.objects.create_superuser(name='root', password='123')

        self.assertEqual(user.name, 'root')
        self.assertEqual(user.email, None)
        self.assertTrue(user.check_password('123'))

    def test_cnpj_user(self):

        payload = {
            'owner_type': 'PJ',
            'cnpj': '12345678910123',
            'email': 'test@example.com',
            'name': 'TestUser',
            'password': 'Testpass123'
        }
        user = User.objects.create(**payload)

        self.assertEqual(user.cnpj, '12345678910123')
        self.assertIsNone(user.cpf)

    def test_create_account(self):

        user = create_user()

        payload = {
            'user': user,
            'agency': '12345',
            'account': '1234567',
        }

        account = Account.objects.create(**payload)

        for param, value in payload.items():
            self.assertEqual(getattr(account, param), value)

    def test_create_account_same_number_defferent_agency(self):

        user1 = create_user()
        user2 = create_user(
            name='Test2', email='Test2@example.com',cpf='12345678911'
        )
        payload1 = {
            'user': user1,
            'agency': '12345',
            'account': '1234567',
        }
        payload2 = {
            'user': user2,
            'agency': '12346',
            'account': '1234567',
        }

        account1 = Account.objects.create(**payload1)
        account2 = Account.objects.create(**payload2)

        self.assertNotEqual(account1.agency, account2.agency)

    def test_address_creation(self):

        user = create_user()

        payload = {
            'user': user,
            'state': 'SP',
            'city': 'São Paulo',
            'district': 'Zona Leste',
            'zip_code': '11111000',
            'street': 'Flower St, 7329',
        }

        address = Address.objects.create(**payload)

        for param, value in payload.items():
            self.assertEqual(getattr(address, param), value)
