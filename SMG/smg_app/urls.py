from django.urls import path

from . import views


urlpatterns = [
    # path('', views.home, name='home'),
    # path("signup", views.signup, name="signup"),
    path("", views.profile, name="user_profile"),
    path("login", views.loginPage, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout, name="logout"),
    path("profile/<username>", views.profile, name="profile"),
    path("editProfile", views.profile_update, name="edit_profile"),
    path("search", views.search, name="search"),
    path("friends/<operation>/<username>", views.change_friend, name="change_friend"),
    path("friend_req/<username>", views.friend_request, name="friend_request"),
    path("friend_req/<username>/s", views.friend_request_s, name="friend_request_s"),
    path("del_friend_req/<operation>/<username>", views.delete_request, name="delete_request"),
    path("friends_page/<username>", views.friendPage, name="friendPage"),
    path("connect", views.connection_page, name="connection_page"),
    path("message/<username>", views.message, name="message"),
    path("send_message", views.send_message, name="send_message"),
    path("get_new_messages/<username>/<time>", views.get_new_messages, name="get_new_messages"),
]
