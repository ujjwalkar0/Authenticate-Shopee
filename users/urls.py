from django.contrib.auth.views import LogoutView
from django.urls import path
from users.views import *

urlpatterns = [
    path('login/',UserLoginView.as_view(),name="login"),
    path('register/',UserRegisterView.as_view(),name="register"),
    path('edit_profile/',UserEditView.as_view(),name="edit_profile"),
    path("logout/", LogoutView.as_view(template_name='users/logout.html'), name="logout"),

]
