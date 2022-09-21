from django.forms import ModelForm
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
