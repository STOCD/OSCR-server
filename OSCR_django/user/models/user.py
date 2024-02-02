""" User Model """

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Our Implementation of the Abstract User"""

    def __str__(self):
        return self.username
