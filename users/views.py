from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.views import LoginView
from users.forms import *

# User Login Page
class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm


# User Register Page
class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'users/register.html'
    success_url = '/user/login'

# User's Data Update Page
class UserEditView(UpdateView):
    form_class = EditForm
    template_name = 'users/edit_profile.html'
    success_url = '/'
    
    def get_object(self):
        return self.request.user
