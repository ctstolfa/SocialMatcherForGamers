from django.contrib import admin
from .models import Games,Schedule, Account, GameMode

# Register your models here.
# admin.site.register(User)
# admin.site.register(login)
# admin.site.register(home)
admin.site.register(Account)
admin.site.register(Games)
admin.site.register(Schedule)
admin.site.register(GameMode)


