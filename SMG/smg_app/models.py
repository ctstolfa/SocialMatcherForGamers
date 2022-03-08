from django.db import models
from django.utils import timezone

# Create your models here.
Max_length = 1023


# account section
class Account(models.Model):
    class Role(models.IntegerChoices):
        USER = 0, "User"
        ADMIN = 1, "Admin"

    class gameStyle(models.IntegerChoices):
        CASUAL = 0, "Casual"
        COMPETITIVE = 1, "Competitive"

    userName = models.CharField(max_length=20, default="")
    role = models.IntegerField(choices=Role.choices)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)
    gameMode = models.IntegerField(choices=gameStyle.choices, default=0)

    def __str__(self):
        return self.userName

    def set_email(self):
        email = self.email

    def get_email(self):
        return self.email

    def set_role(self):
        role = self.role

    def get_role(self):
        return self.role


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