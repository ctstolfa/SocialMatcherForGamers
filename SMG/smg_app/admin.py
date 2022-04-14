from django.contrib import admin
from .models import Account, Friend, FriendRequest

# Register your models here.

admin.site.register(Account)
admin.site.register(Friend)
admin.site.register(FriendRequest)
