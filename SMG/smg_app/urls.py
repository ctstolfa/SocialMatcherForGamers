from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    # path("signup", views.signup, name="signup"),
    path('', views.loginPage, name="LoginPage"),
    path('register', views.register, name="register"),
    path("logout", views.logout, name="logout"),
    path("profile/<username>", views.profile, name="profile"),
    path('editProfile', views.profile_update, name="edit_profile"),
    path('search', views.search, name='search'),
    path('friends/<operation>/<username>', views.change_friend, name='change_friend'),
    path('connect', views.connection_page, name='connection_page'),
]
