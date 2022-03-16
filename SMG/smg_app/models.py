from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField

# Create your models here.
Max_length = 1023


# account section
class Account(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    class Role(models.IntegerChoices):
        USER = 0, "User"
        ADMIN = 1, "Admin"

    class GameStyle(models.TextChoices):
        CASUAL = "Casual"
        COMPETITIVE = "Competitive"


    Genres = (
        ('MOBA','MOBA'),
        ('Shooters','Shooters'),
        ('Platformer','Platformer'),
        ('RPG','RPG'),
        ('Action-adventure','Action-adventure'),
        ('RTS','RTS'),
        ('Puzzles','Puzzles'),
        ('ParyGames','ParyGames'),
        ('Survival','Survival'),
        ('Horror','Horror'),
    )

    genres = MultiSelectField(choices=Genres)

    days = (
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    )

    schedule = MultiSelectField(choices=days)

    times = (
        ('Morning','Morning'),
        ('Afternoon','Afternoon'),
        ('Night','Night'),
        ('Midnight','Midnight'),
    )

    time = models.TextField(choices=times)

    role = models.IntegerField(choices=Role.choices)
    gameStyle = models.TextField(choices=GameStyle.choices)

    def __str__(self):
        return str(self.user)

    def set_role(self):
        role = self.role

    def get_role(self):
        return self.role

    def set_gameStyle(self):
        gameStyle = self.gameStyle

    def get_gameStyle(self):
        return self.gameStyle


# games section
class Games(models.Model):
    def __str__(self):
        return self.Genres


# schedule section
class Schedule(models.Model):
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)
    time = models.DateTimeField(default=timezone.now)
    #account = models.ForeignKey(Account, on_delete=models.CASCADE)

    # games = models.ForeignKey(Games, on_delete=models.CASCADE)