from django.db import models

# Create your models here.
Max_length = 1023

class Account(models.Model):
    class Role(models.IntegerChoices):
        USER = 0, "User"
        ADMIN = 1, "Admin"

    name = models.CharField(max_length=Max_length)
    role = models.IntegerField(choices=Role.choices)
    email = models.EmailField()
    password = models.CharField(max_length=Max_length)

    def __str__(self):
        return  self.name

    def set_email(self):
        email = self.email

    def get_email(self):
        return self.email

    def set_role(self):
        role = self.role

    def get_role(self):
        return self.role