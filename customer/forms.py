from dataclasses import field
from django.forms import ModelForm
from customer.models import Customer

class RegisterCustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ('name',)

    def __init__(self, *args, **kwargs):
        super(RegisterCustomerForm, self).__init__( *args, **kwargs)

        for i in self.fields:
            self.fields[i].label = False
            self.fields[i].widget.attrs['class'] = 'form-control'
            self.fields[i].widget.attrs['placeholder'] = ' '.join([i.capitalize() for i in i.split('_')])
