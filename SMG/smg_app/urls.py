from django.urls import path
from . import views



urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path('', views.Login_Page, name="Login_page"),
    # path('', views.home, name='home'),
    path('signup', views.signup, name="signup"),
]
