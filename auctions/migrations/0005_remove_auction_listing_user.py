# Generated by Django 3.2.5 on 2021-08-17 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_remove_auction_listing_item_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction_listing',
            name='user',
        ),
    ]
