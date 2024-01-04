from django.db.models.signals import post_migrate
from django.apps import AppConfig

def create_initial_categories(sender, **kwargs):
    from .models import Category  # Import Category within the signal function
    categories = ['Art', 'Vintage', 'Music', 'Electronics']

    for category in categories:
        category_exists = Category.objects.filter(name=category).exists()
        if not category_exists:
            Category.objects.create(name=category)

def connect_signals(sender, **kwargs):
    post_migrate.connect(create_initial_categories, sender=sender)

# Connect signals within the ready method
AppConfig.ready = connect_signals
