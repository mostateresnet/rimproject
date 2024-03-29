import json
from django import forms
from django.utils.translation import ugettext_lazy as _
from rim.models import Equipment


class EquipmentForm(forms.ModelForm):

    json_fields = forms.fields.CharField(
        required=False, widget=forms.HiddenInput(),)

    def __init__(self, *args, **kwargs):
        # Override __init__ to set minimum values of numbers
        super(EquipmentForm, self).__init__(*args, **kwargs)
        self.fields['count'].widget.attrs['min'] = 0
        self.fields['purchase_price'].widget.attrs['min'] = 0
        self.fields['json_fields'].initial = json.dumps(
            {"storage": self.instance.storage, "GPU": self.instance.GPU, "network_cards": self.instance.network_cards, "displays": self.instance.displays})
        if self.instance._state.adding:
            # "Add" page allows bulk serial numbers
            self.fields['serial_no'].widget = forms.Textarea()
            self.fields['serial_no'].label = _('Serial number(s)')

    class Meta:
        model = Equipment
        exclude = ['latest_checkout', 'storage', 'GPU',
                   'network_cards', 'displays', 'users_info']

    def clean_serial_no(self):
        data = self.cleaned_data['serial_no']
        data = data.upper()
        if self.instance._state.adding:
            # "Add" page allows bulk serial numbers
            data = set(x for x in data.splitlines() if x)
        if not data:
            raise forms.ValidationError(
                self.fields['serial_no'].error_messages['required'])
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
        dynamic_json = json.loads(self.cleaned_data['json_fields'])
        self.instance.storage = dynamic_json['storage']
        self.instance.GPU = dynamic_json['GPU']
        self.instance.network_cards = dynamic_json['network_cards']
        self.instance.displays = dynamic_json['displays']
        return super(EquipmentForm, self).save(commit)
