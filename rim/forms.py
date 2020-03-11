from django import forms
from rim.models import Equipment


class EquipmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        #Override __init__ to set minimum values of numbers
        super(EquipmentForm, self).__init__(*args, **kwargs)
        self.fields['count'].widget.attrs['min'] = 0
        self.fields['usb_ports'].widget.attrs['min'] = 0
        self.fields['purchase_price'].widget.attrs['min'] = 0

    class Meta:
        model = Equipment
        exclude = ['latest_checkout']
