# Generated by Django 3.2.5 on 2021-09-05 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0026_remove_user_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='watched',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='item_id',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='item_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auctions.auction_listing'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='user_id',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auctions.user'),
            preserve_default=False,
        ),
    ]