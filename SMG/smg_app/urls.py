from django.urls import path

from . import views

urlpatterns = [
    # path(r'^admin/', admin.site.urls),
    path('login', views.login, name="login"),
    # path('', views.home, name='home'),
    path('register', views.register, name="register"),
]
