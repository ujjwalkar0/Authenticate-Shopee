from django.forms import ModelForm
from business.models import Shop

class ShopForm(ModelForm):
    class Meta:
        model = Shop
        exclude = ('user_id',)

    def __init__(self, *args, **kwargs):
        super(ShopForm, self).__init__( *args, **kwargs)

        for i in self.fields:
            self.fields[i].label = False
            self.fields[i].widget.attrs['class'] = 'form-control'
            self.fields[i].widget.attrs['placeholder'] = ' '.join([i.capitalize() for i in i.split('_')])

        # self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        # self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        # self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        # self.fields['username'].widget.attrs['placeholder'] = 'Username'
        # self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        # self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
