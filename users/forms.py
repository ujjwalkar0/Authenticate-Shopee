from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm, AuthenticationForm
from users.models import Users
from django.forms import *

# User Login Form
class LoginForm(AuthenticationForm):    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__( *args, **kwargs)

        for i in self.fields:
            self.fields[i].label = False
            self.fields[i].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

# User Register Form
class SignUpForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ('first_name','last_name','username','email','user_type','password1','password2')
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__( *args, **kwargs)

        for i in self.fields:
            self.fields[i].label = False
            self.fields[i].widget.attrs['class'] = 'form-control'

        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

# User Data Update Form
class EditForm(UserChangeForm):
    email = EmailField(widget=EmailInput(attrs={"class":"form-control"}) )
    
    class Meta:
        model = Users
        fields = ('first_name','last_name','username','email', 'user_type')
    
    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__( *args, **kwargs)

        for i in self.fields:
            self.fields[i].label = False
            self.fields[i].widget.attrs['class'] = 'form-control'

        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'

# Change Password Form
class PasswordChangingForm(PasswordChangeForm):
    old_password = CharField(max_length=100,widget=PasswordInput(attrs={"class":"form-control",'type':'password'}))
    new_password1 = CharField(max_length=100,widget=PasswordInput(attrs={"class":"form-control",'type':'password'}))
    new_password2 = CharField(max_length=100,widget=PasswordInput(attrs={"class":"form-control",'type':'password'}))

     
    class Meta:
        model = Users
        fields = ('old_password','new_password1','new_password2')

