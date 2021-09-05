# Generated by Django 3.2.5 on 2021-09-05 15:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_auto_20210905_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='item_id',
            field=models.ManyToManyField(related_name='item_watched', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='user_id',
            field=models.ManyToManyField(related_name='user_watching', to='auctions.Auction_listing'),
        ),
    ]