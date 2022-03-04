from django.contrib import admin
from .models import Games, Schedule, Account

# Register your models here.

admin.site.register(Account)
admin.site.register(Games)
admin.site.register(Schedule)

