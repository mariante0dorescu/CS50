# Generated by Django 5.0 on 2023-12-29 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_remove_listing_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
