# Generated by Django 3.2.5 on 2021-08-16 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210816_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction_listing',
            name='item_id',
        ),
    ]