# Generated by Django 4.1.6 on 2023-02-07 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('owner_type', models.CharField(choices=[('PF', 'Fisica'), ('PJ', 'Juridica')], default='PF', max_length=2)),
                ('cpf', models.CharField(max_length=11, null=True, unique=True)),
                ('cnpj', models.CharField(max_length=14, null=True, unique=True)),
                ('email', models.EmailField(max_length=255, null=True, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=45)),
                ('district', models.CharField(max_length=45)),
                ('zip_code', models.CharField(max_length=8)),
                ('street', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency', models.CharField(max_length=5)),
                ('account', models.CharField(max_length=7)),
                ('account_type', models.CharField(choices=[('CC', 'Corrente'), ('CP', 'Poupanca')], default='CC', max_length=2)),
                ('is_active', models.BooleanField(default=True)),
                ('balance', models.IntegerField(default=0)),
                ('register_date', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('account', 'agency')},
            },
        ),
    ]
