# Generated by Django 3.2.5 on 2021-09-05 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0025_user_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='salary',
        ),
    ]