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
        ('PartyGames','PartyGames'),
        ('Survival','Survival'),
        ('Horror','Horror'),
    )

    genres = MultiSelectField(choices=Genres, default=0)

    days = (
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    )

    schedule = MultiSelectField(choices=days, default=0)

    times = (
        ('Morning','Morning'),
        ('Afternoon','Afternoon'),
        ('Night','Night'),
        ('Midnight','Midnight'),
    )

    time = models.TextField(choices=times, default=timezone.now)

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


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.OneToOneField(User, related_name='owner', null=True, on_delete=models.CASCADE)

    @classmethod
    def add_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, old_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(old_friend)

    def __str__(self):
        return str(self.current_user)+"'s friends"


class FriendRequest(models.Model):
    sender = models.ForeignKey(User, null=True, related_name='sender1', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='receiver1')

    def __str__(self):
        return str(self.receiver)+"'s requests"
