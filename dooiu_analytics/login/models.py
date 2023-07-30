from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from services import database_services


class UserProfile(models.Model):


    id = models.IntegerField(primary_key=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    country_code = models.CharField(max_length=5)
    user_type = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def to_dict(self):
        return {
            'id': self.id,
            'phone_number': self.phone_number,
            'email': self.email,
            'country_code': self.country_code,
            'user_type': self.user_type,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone_number})"

