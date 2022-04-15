# Generated by Django 4.0.2 on 2022-04-15 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres', multiselectfield.db.fields.MultiSelectField(choices=[('MOBA', 'MOBA'), ('Shooters', 'Shooters'), ('Platformer', 'Platformer'), ('RPG', 'RPG'), ('Action-adventure', 'Action-adventure'), ('RTS', 'RTS'), ('Puzzles', 'Puzzles'), ('PartyGames', 'PartyGames'), ('Survival', 'Survival'), ('Horror', 'Horror')], default=0, max_length=84)),
                ('schedule', multiselectfield.db.fields.MultiSelectField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default=0, max_length=56)),
                ('time', models.TextField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Night', 'Night'), ('Midnight', 'Midnight')], default=django.utils.timezone.now)),
                ('role', models.IntegerField(choices=[(0, 'User'), (1, 'Admin')])),
                ('gameStyle', models.TextField(choices=[('Casual', 'Casual'), ('Competitive', 'Competitive')])),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
