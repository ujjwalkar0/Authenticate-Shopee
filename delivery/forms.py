from django.forms import ModelForm
from delivery.models import DeliveryAgent

class DeliveryAgentForm(ModelForm):
    class Meta:
        model = DeliveryAgent
        exclude = ('user_id',)
    
    def __init__(self, *args, **kwargs):
        super(DeliveryAgentForm, self).__init__(*args, **kwargs)

        for i in self.fields:
            self.fields[i].label = False
            self.fields[i].widget.attrs['class'] = 'form-control'
            self.fields[i].widget.attrs['placeholder'] = ' '.join([i.capitalize() for i in i.split('_')])
