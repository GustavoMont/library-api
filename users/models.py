from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group

class ManagerUser(BaseUserManager):

    def create_superuser(self, email, username, first_name, password, cpf,**other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, first_name, password, cpf,**other_fields)

    def create_user(self, email, username, first_name, password, cpf,**other_fields):

        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name, cpf=cpf,**other_fields)
        user.set_password(password)
        if not user.is_superuser:
            user.groups.add(Group.objects.get(name='CLIENT'))
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField('email address', unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    can_borrow = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cpf = models.CharField(max_length=11, unique=True, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = ManagerUser()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'cpf', 'first_name']

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.first_name