# Generated by Django 5.0 on 2023-12-29 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_listing_options_listing_duration_listing_end_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='end',
        ),
    ]