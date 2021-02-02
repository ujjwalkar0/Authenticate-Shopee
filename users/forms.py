from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm, UserChangeForm
from .models import Users
from django import forms

choices = [('Business', 'Business'), ('Delivery Boy', 'Delivery Boy'), ('Customer', 'Customer')]

class SignUpForm(UserCreationForm):
    firstname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    lastname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))

    
    class Meta:
        model = Users
        fields = ('firstname','lastname','username','email','user_type','password1','password2')
        widgets = {
            "user_type" : forms.Select(choices=choices,attrs={"class":"form-control","placeholder":"Name of the Product"}),
        }


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__( *args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
class EditForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}) )
    firstname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    lastname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))

    
    class Meta:
        model = Users
        fields = ('firstname','lastname','username','email','password')

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control",'type':'password'}))
    new_password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control",'type':'password'}))
    new_password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control",'type':'password'}))

     
    class Meta:
        model = Users
        fields = ('old_password','new_password1','new_password2')

