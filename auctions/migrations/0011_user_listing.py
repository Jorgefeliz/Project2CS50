# Generated by Django 3.2.5 on 2021-08-21 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_remove_auction_listing_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
            ],
        ),
    ]
