from django.urls import path
from . import views



urlpatterns = [
#<<<<<<< Search
    path('', views.home, name='home'),
    path('login', views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("signup", views.signup, name="signup"),
    path('search', views.search, name='search'),
#=======
    path(r'^admin/', admin.site.urls),
    path('', views.Login_Page, name="Login_page"),
    # path('', views.home, name='home'),
    path('signup', views.signup, name="signup"),
#>>>>>>> main
]
