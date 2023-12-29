from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


def image_path(instance, filename):
    user_id = instance.user.id
    return f'{user_id}/{filename}'


class User(AbstractUser):
    pass


class Listing(models.Model):
    pass


class Bid(models.Model):
    pass


class Comment(models.Model):
    pass
