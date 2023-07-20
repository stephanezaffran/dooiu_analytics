from django.contrib.auth.backends import BaseBackend
from login.models import User


class NoLastLoginBackend(BaseBackend):
    def user_can_authenticate(self, user):
        # Override to always return True, so it doesn't check the last_login field
        return True

    def authenticate(self, request, phone_number=None, password=None, **kwargs):
        try:
            user = User.objects.get(phone_number=phone_number)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

