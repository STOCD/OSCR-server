""" Base Model """

from django.db import models


class BaseModel(models.Model):
    """Base Model"""

    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True


class BaseNameModel(models.Model):
    """Base Model with Name field"""

    name = models.TextField(primary_key=True)

    class Meta:
        abstract = True
