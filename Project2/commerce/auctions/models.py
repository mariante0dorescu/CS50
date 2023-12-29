from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


def image_path(instance, filename):
    #get user id from listing
    user_id = instance.user.id
    
    #return the file path
    return f'{user_id}/{filename}'

#validate price to be greater than 0, raise validation error
def validate_price(value):
    if value <= 0:
        raise ValidationError('Price must be greater than 0')

class User(AbstractUser):
    pass

class Listing(models.Model):

    DURATION_CHOICES = (
    (1, '1 hour'),
    (3, '3 hours'),
    (12, '12 hours'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to = image_path)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_price])
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField()
    duration = models.PositiveIntegerField(choices=DURATION_CHOICES)

    @property
    def calculate_end_date(self):
        if self.duration == 1:
            return self.start_date + timezone.timedelta(hours=1)
        elif self.duration == 3:
            return self.start_date + timezone.timedelta(hours=3)
        elif self.duration == 12:
            return self.start_date + timezone.timedelta(hours=12)
        else:
            # Handle other cases or raise an exception
            return None

    def save(self, *args, **kwargs):
        if not self.end_date:
            # Set end_date using the calculate_end_date property
            self.end_date = self.calculate_end_date
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['end_date']
    
class Bids(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    bid = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_price])

    def __str__(self):
        return str(self.bid)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment