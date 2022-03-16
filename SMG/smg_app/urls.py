from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.loginPage, name="LoginPage"),
    path('register', views.register, name="register"),
    path("logout", views.logout, name="logout"),
    path("profile/<username>", views.profile, name="profile"),
    #path("signup", views.signup, name="signup"),
    path('search', views.search, name='search'),
]
