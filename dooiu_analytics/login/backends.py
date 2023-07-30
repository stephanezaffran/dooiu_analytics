# from django.contrib.auth import get_user_model
#
# User = get_user_model()
# from django.db import connection
#
# class UserAuthBackend:
#     def authenticate(self, request, phone_number=None, password=None):
#         try:
#             user = User.objects.get(phone_number=phone_number)
#             if user.password == password:
#                 return user
#         except User.DoesNotExist:
#             return None
#
#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None
#
#
