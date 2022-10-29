from django.forms import *
from products.models import Product
from .models import Categories

class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("user_id","Pin_No")

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__( *args, **kwargs)

        for i in self.fields:
            self.fields[i].label = False
            self.fields[i].widget.attrs['class'] = 'form-control'
            self.fields[i].widget.attrs['placeholder'] = ' '.join([i.capitalize() for i in i.split('_')])
        
        self.fields['catagory'].queryset = Categories.objects.filter(is_approved=True)


class LaptopForm(Form):
    processor = CharField(label='Processor', max_length=100)
    ram = CharField(label='RAM', max_length=100)
    os = CharField(label='Operating System', max_length=100)
    storage = CharField(label='Storage', max_length=100)
    display = CharField(label='display', max_length=100)
    warranty = CharField(label='warranty', max_length=100)

    def __init__(self, *args, **kwargs):
        super(LaptopForm, self).__init__( *args, **kwargs)

        for i in self.fields:
            self.fields[i].widget.attrs['placeholder'] =  self.fields[i].label #' '.join([i.capitalize() for i in i.split('_')])
            self.fields[i].label = False
            self.fields[i].widget.attrs['class'] = 'form-control'
