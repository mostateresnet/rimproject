from django import forms
from django.utils.translation import ugettext_lazy as _
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

    def __init__(self, *args, **kwargs):
        super(EquipmentForm, self).__init__(*args, **kwargs)

        if self.instance._state.adding:
            # "Add" page allows bulk serial numbers
            self.fields['serial_no'].widget = forms.Textarea()
            self.fields['serial_no'].label = _('Serial number(s)')

    def clean_serial_no(self):
        data = self.cleaned_data['serial_no']
        data = data.upper()
        if self.instance._state.adding:
            # "Add" page allows bulk serial numbers
            data = set(x for x in data.splitlines() if x)
        if not data:
            raise forms.ValidationError(self.fields['serial_no'].error_messages['required'])
        return data

    def save(self, commit=True):
        if self.instance._state.adding:
            # "Add" page allows bulk serial numbers
            new_objects = []
            for serial_no in self.cleaned_data['serial_no']:
                self.instance.pk = None
                self.instance.serial_no = serial_no
                new_objects.append(super(EquipmentForm, self).save(commit))
            return new_objects[0]
        return super(EquipmentForm, self).save(commit)
