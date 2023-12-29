#returns a image path based on user id and image
def image_path(instance, filename):
    user_id = instance.user.id
    listing_id = instance.id

    return f'uploads/{user_id}/{listing_id:02d}/{filename}'

#validate price to be greater than 0, raise validation error
def validate_price(value):
    if value < 0:
        raise ValidationError('Price must be greater than 0')

#validate date not be in the past, raise validation error
def validate_date(value):
    if value <= timezone.now():
        raise ValidationError('End date must be in the future')