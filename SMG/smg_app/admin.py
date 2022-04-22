from django.contrib import admin

from .models import Account, Friend, FriendRequest, Message


# Register your models here.

admin.site.register(Account)
admin.site.register(Friend)
admin.site.register(FriendRequest)
admin.site.register(Message)
