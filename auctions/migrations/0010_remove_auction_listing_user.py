# Generated by Django 3.2.5 on 2021-08-17 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auction_listing_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction_listing',
            name='user',
        ),
    ]
