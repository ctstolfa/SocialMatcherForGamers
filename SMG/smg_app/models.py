from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

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
    name = models.CharField(max_length=20)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    # games = models.ForeignKey(Games, on_delete=models.CASCADE)