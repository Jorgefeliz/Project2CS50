# Generated by Django 3.2.5 on 2021-09-04 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20210904_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_listing',
            name='item_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user_listing',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
