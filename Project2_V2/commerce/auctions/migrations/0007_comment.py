# Generated by Django 5.0 on 2024-01-02 09:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_bid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('listing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.listing')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]