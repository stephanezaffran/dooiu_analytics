from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from services import database_services
from functools import wraps
from django.shortcuts import render, redirect


def custom_authenticate(phone_number=None, password=None):
    user = database_services.get_user_data(phone_number)
    if user and user[8] == password:
        return user
    return None

# def create_user(phone_number, password=None):
#     if not phone_number:
#         raise ValueError('Le numéro de téléphone doit être défini.')
#
#     user = self.model(phone_number=phone_number)
#     user.set_password(password)
#     user.save(using=self._db)
#     return user
#
