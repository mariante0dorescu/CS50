from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


def image_path(instance, filename):
    user_id = instance.user.id
    #listing_id = instance.id

    #return f'uploads/{user_id}/{listing_id:02d}/{filename}'
    return f'{user_id}/{filename}'


class User(AbstractUser):
    pass

class Listing(models.Model):
    pass