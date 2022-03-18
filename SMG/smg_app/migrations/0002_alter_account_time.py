# Generated by Django 4.0.2 on 2022-03-17 20:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('smg_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='time',
            field=models.TextField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Night', 'Night'), ('Midnight', 'Midnight')], default=datetime.datetime(2022, 3, 17, 20, 26, 21, 414237, tzinfo=utc)),
        ),
    ]