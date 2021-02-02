# from .views import RegisterAPI
from knox import views as knox_views
from .views import *
# from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, include
from .models import Users
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

urlpatterns = [

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))


    path('register/api', RegisterAPI.as_view(), name='registerapi'),
    # path('login/api', LoginAPIView.as_view(), name='loginapi'),
    path('logout/api', knox_views.LogoutView.as_view(), name='logoutapi'),
    path('logoutall/api', knox_views.LogoutAllView.as_view(), name='logoutallapi'),


    path('register/',UserRegisterView.as_view(),name="register"),
    path('edit_profile/',UserEditView.as_view(),name="edit_profile"),
    path('password/',PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success/',views.password_success,name='password_success'),

    path('profile/<int:pk>',ProfileView.as_view(),name="profile"),

]
