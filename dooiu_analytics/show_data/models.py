from django.db import models
from login.models import User

class Data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    value = models.FloatField()