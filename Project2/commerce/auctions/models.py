from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import MinValueValidator

#returns an image path based on user id
def image_path(instance, filename):
    user_id = instance.user.id
    return f'{user_id}/{filename}'


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class User(AbstractUser):
    pass

class Listing(models.Model):

    DURATION = (
        (1, '1 hour'),
        (3, '3 hours'),
        (12, '12 hours'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=65, null=False, blank=True)
    text = models.TextField(null=True)
    image = models.FileField(upload_to=image_path, blank=True, null=False)
    starting_bid = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(limit_value=0.01)], default=0.0)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(null=True, blank=True)
    duration = models.PositiveIntegerField(default=1, choices=DURATION)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(default=False)

    @property
    def calculate_end(self):
        if self.duration == 1:
            return self.start + timezone.timedelta(hours=1)
        elif self.duration == 3:
            return self.start + timezone.timedelta(hours=3)
        elif self.duration == 12:
            return self.start + timezone.timedelta(hours=12)
        else:
            return self.start + timezone.timedelta(hours=12)

    @property
    def current_bid(self):
        latest_bid = self.bids.order_by('-bid').first()
        return latest_bid.bid if latest_bid else None

    def save(self,*args, **kwargs):
        self.end = self.calculate_end
        self.active = self.end > timezone.now()
        super().save(*args, **kwargs)

    def image_url(self):
        return self.image.url if self.image else None

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['start']

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids', null=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids', null=True, blank=True)
    bid = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    
    def __str__(self):
        return str(self.bid)


class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comment', null=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment', null=False, blank=True)
    comment = models.TextField(max_length=200, null=False, blank=True)
    
    def __str__(self):
        return self.comment

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist', null=False, blank=True)
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='item', null=False, blank=True)

    def __str__(self):
        return self.item.id