from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm, UserChangeForm
from users.models import Users
choices = Catagoriess.objects.all().values_list('name','name')

# choices = [('Business', 'Business'), ('Delivery Boy', 'Delivery Boy'), ('Customer', 'Customer')]
# Subscription = [('Rs. 100 (API)', 'Rs. 100 (API)'), ('Rs. 100 (Ads. at users Account)', 'Rs. 100 (Ads. at users Account)'), ('Rs. 150 for Both', 'Rs. 150 for Both')]

# class ShopForm(UserCreationForm):
    
#     class Meta:
#         model = Shop
#         fields = '__all__'
#         widgets = {
#             # "user_type" : forms.Select(choices=choices,attrs={"class":"form-control","placeholder":"Name of the Product"}),
#         }


class OrderForm(forms.ModelForm):
    class Meta:
        model = order
        fields = '__all__'


class IPForm(forms.ModelForm):
    class Meta:
        model = IP
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            "username" : forms.TextInput(attrs={"class":"form-control"}), 
            "title" : forms.TextInput(attrs={"class":"form-control","placeholder":"Name of the Product"}), 
            "catagory" : forms.Select(choices=choices,attrs={"class":"form-control"}), 
            "body" : forms.Textarea(attrs={"class":"form-control"}), 
        }
        labels = {
        "body": "Description",
        "image":"Image of Your Product ( Image 1)",
        "image2":"Image of Your Product ( Image 2)",
        }

class PhonesPostForm(forms.ModelForm):
    class Meta:
        model = Phones
        fields = '__all__'
        widgets = {
            'Product_name' : forms.TextInput(attrs={"class":"form-control"}),
            'username' : forms.TextInput(attrs={"class":"form-control"}),
            'by_info' : forms.TextInput(attrs={"class":"form-control"}),
            'Product_url' : forms.TextInput(attrs={"class":"form-control"}),
            'Product_img' : forms.TextInput(attrs={"class":"form-control"}),
            'Product_price' : forms.TextInput(attrs={"class":"form-control"}),
            'prod_des' : forms.TextInput(attrs={"class":"form-control"}),
            'feature' : forms.TextInput(attrs={"class":"form-control"}),
            'cust_review' : forms.TextInput(attrs={"class":"form-control"}),
        }

# choices = [('Business', 'Business'), ('Delivery Boy', 'Delivery Boy'), ('Customer', 'Customer')]
fuel_ = [('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('CNG', 'CNG'), ('Electric', 'Electric'), ('LPG', 'LPG')]
seller_type_ = [('Dealer', 'Dealer'), ('Individual', 'Individual'), ('Trustmark 0', 'Trustmark 0')]
transmission_ = [('Manual', 'Manual'), ('Automatic', 'Automatic')]
owner_ = [('First Owner', 'First Owner'), ('Second Owner', 'Second Owner'), ('Third Owner', 'Third Owner'), ('Fourth & Above Owner', 'Fourth & Above Owner'), ('Test Drive Car', 'Test Drive Car')]
# Petrol":"0","Diesel":"1","CNG":"2","Electric":"3","LPG

# CarTestForm
class CarTestForm(forms.ModelForm):
    class Meta:
        model = TestCar
        fields = '__all__'
        widgets = {
            'year' : forms.TextInput(attrs={"class":"form-control"}),
            # 'selling_price' : forms.TextInput(attrs={"class":"form-control"}),
            'km_driven' : forms.TextInput(attrs={"class":"form-control"}),
            'fuel' : forms.Select(choices=fuel_,attrs={"class":"form-control"}), 
            'seller_type' : forms.Select(choices=seller_type_,attrs={"class":"form-control"}), 
            'transmission' : forms.Select(choices=transmission_,attrs={"class":"form-control"}), 
            'owner' : forms.Select(choices=owner_,attrs={"class":"form-control"}), 
        }


class CarPostForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={"class":"form-control"}),
            # 'image' : forms.TextInput(attrs={"class":"form-control"}),
            'year' : forms.TextInput(attrs={"class":"form-control"}),
            'selling_price' : forms.TextInput(attrs={"class":"form-control"}),
            'km_driven' : forms.TextInput(attrs={"class":"form-control"}),
            'fuel' : forms.Select(choices=fuel_,attrs={"class":"form-control"}), 
            'seller_type' : forms.Select(choices=seller_type_,attrs={"class":"form-control"}), 
            'transmission' : forms.Select(choices=transmission_,attrs={"class":"form-control"}), 
            'owner' : forms.Select(choices=owner_,attrs={"class":"form-control"}), 
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            "title" : forms.TextInput(attrs={"class":"form-control","placeholder":"Name of the Product"}), 
            "username" : forms.TextInput(attrs={"class":"form-control"}), 
            "catagory" : forms.Select(choices=choices,attrs={"class":"form-control"}), 
            "body" : forms.Textarea(attrs={"class":"form-control"}), 
        }
        labels = {
        "body": "Description",
        "image":"Image of Your Product ( Image 1)",
        "image2":"Image of Your Product ( Image 2)",
        }

class UserEditForm(UserChangeForm):
    firstname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    lastname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))

    
    class Meta:
        model = Users
        fields = ('firstname','lastname','username')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}) )
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))

    
    class Meta:
        model = Profile
        fields = ('first_name','last_name','username','email','password','image','address','mobile_no','bio','website_url','facebook_url','twitter_url','linkdin_url')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__( *args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
class Orders(forms.ModelForm):
    class Meta:
        model = order
        fields = '__all__'
        widgets = {
            "address" : forms.Textarea(attrs={"class":"form-control"}), 
        }

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            'shop_name',
            'address',
            'phone_no',
            'email_id',
            'website',
            'Pin_No',
            # 'Subscription',
        ]
        widgets = {
            'shop_name' :  forms.TextInput(attrs={"class":"form-control"}), 
            'address' :  forms.TextInput(attrs={"class":"form-control"}), 
            'phone_no' :  forms.TextInput(attrs={"class":"form-control"}), 
            'email_id' :  forms.TextInput(attrs={"class":"form-control"}), 
            'website' :  forms.TextInput(attrs={"class":"form-control"}), 
            'Pin_No' :  forms.TextInput(attrs={"class":"form-control"}), 

            # 'Subscription' : forms.Select(choices=Subscription,attrs={"class":"form-control"}),
        }
