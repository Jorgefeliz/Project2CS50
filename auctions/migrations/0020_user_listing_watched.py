# Generated by Django 3.2.5 on 2021-09-04 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_auto_20210904_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_listing',
            name='watched',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
