# Generated by Django 5.0 on 2024-01-02 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_listing_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='user_id',
            new_name='user',
        ),
    ]
