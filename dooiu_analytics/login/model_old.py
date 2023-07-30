#
# from django.db import connection
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models
# from django.contrib.auth.hashers import check_password
#
#
# class UserManager(BaseUserManager):
#
#     def authenticate(self, request, phone_number=None, password=None):
#
#         try:
#             # Connect to the MySQL database using the credentials from settings.py
#
#             with connection.cursor() as cursor:
#
#                 print(f"authenticate: select * from user where phoneNumber = '{phone_number}' and password = '{password}';")
#                 cursor.execute(f"select * FROM user where phoneNumber = '{phone_number}' and password = '{password}';")
#                 user_data = cursor.fetchone()
#                 print(f"user_data:  {user_data}")
#
#                 if user_data:
#                     user = self.model(phone_number=user_data[3])  # Assuming phone_number is in the second column
#                     print(f"entered to user_data : {user}  password: {user_data[8]} ")
#                     if password == user_data[8]:
#                         print(f"password: {user_data[8]}")
#                         return user
#         except Exception as e:
#             print(f"exception authenticate: {e.__str__()}")
#             # Handle any exceptions here (e.g., database connection error)
#             return None
#
#         return None
#
#     def create_user(self, phone_number, password=None):
#         if not phone_number:
#             raise ValueError('Le numéro de téléphone doit être défini.')
#
#         user = self.model(phone_number=phone_number)
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#
#     def create_superuser(self, phone_number, password):
#         user = self.create_user(phone_number, password)
#         user.is_admin = True
#         user.save(using=self._db)
#
#         return user
#
#
# class User(AbstractBaseUser):
#     phone_number = models.CharField(max_length=20, unique=True, db_column='phoneNumber')
#     password = models.CharField(max_length=128, db_column='password')
#
#     objects = UserManager()
#
#     # Assuming phoneNumber is the username field
#     USERNAME_FIELD = 'phone_number'
#     # Add any other required fields here
#
#     class Meta:
#         managed = False
#         db_table = 'user'
#
#     def __str__(self):
#         return self.phone_number
#
#     def has_perm(self, perm, obj=None):
#         return True
#
#     def has_module_perms(self, app_label):
#         return True
#
#     @property
#     def is_staff(self):
#         return False
