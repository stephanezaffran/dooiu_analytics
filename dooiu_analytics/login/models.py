from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    # def authenticate(self, request, phone_number=None, password=None):
    #     try:
    #         user = self.model._default_manager.get(phone_number=phone_number)
    #         if user.check_password(password):
    #             return user
    #     except self.model.DoesNotExist:
    #         return None

    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError('Le numéro de téléphone doit être défini.')

        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(phone_number, password)
        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=20, unique=True, db_column='phoneNumber')
    password = models.CharField(max_length=128, db_column='password')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    PASSWORD_FIELD = 'password'

    objects = UserManager()


    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
            return self.is_admin
