from django.db import models


class UserInfo():
    user = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
