# Generated by Django 3.2.5 on 2021-09-04 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_auto_20210904_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bids',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='user_id',
        ),
    ]
