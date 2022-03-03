from django.contrib import admin
from .models import Games,Schedule, Account

# Register your models here.
#<<<<<<< Search
from .models import Account

admin.site.register(Account)
#=======
# admin.site.register(User)
# admin.site.register(login)
# admin.site.register(home)
admin.site.register(Account)
admin.site.register(Games)
admin.site.register(Schedule)



#>>>>>>> main
