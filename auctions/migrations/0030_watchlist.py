# Generated by Django 3.2.5 on 2021-09-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0029_delete_watchlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_pk', models.IntegerField()),
                ('item_pk', models.IntegerField()),
            ],
        ),
    ]
