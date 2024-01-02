from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator

#returns an image path based on user id
def image_path(instance, filename):
    user_id = instance.user.id
    return f'{user_id}/{filename}'


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    image = models.FileField(upload_to=image_path, blank=True, null=False)
    starting = models.DecimalField(max_digits=3, decimal_places=2,validators=[MinValueValidator(limit_value=1)], default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=True, related_name='category')
    active = models.BooleanField(default=True)

    def image_url(self):
        return self.image.url if self.image else None

    def __str__(self):
        return self.title

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=False, blank=True, related_name="user_bid")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE,null=True, blank=True, related_name="listing_bid")
    bid = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return str(self.bid)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=False, blank=True, related_name="user_comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE,null=True, blank=True, related_name="listing_comments")
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment

class Watching(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=False, blank=True, related_name="user_watching")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE,null=True, blank=True, related_name="watching_listing")