import re
import json
from django import forms
from django.utils.translation import ugettext_lazy as _
from rim.models import Equipment, Client, Location, Checkout


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


class CheckoutClientForm(forms.ModelForm):
    def clean(self):
        if 'name' in self.cleaned_data:
            name = self.cleaned_data['name']
            bpn = ''
            bpn_matches = Client.bpn_validator.regex.search(name)

            if bpn_matches:
                bpn = bpn_matches.group(0)
                name = name.replace(bpn, '')

            name = ' '.join(name.split())
            if name == name.lower():
                name = name.title()

            bpn = bpn.upper()

            return {'name': name or bpn, 'bpn': bpn}

        return self.cleaned_data

    def save(self, commit=True):
        self.instance = super(CheckoutClientForm, self).save(commit=False)

        if self.cleaned_data['bpn']:
            query = {'bpn__iexact': self.cleaned_data['bpn']}
        else:
            query = {'name__iexact': self.cleaned_data['name']}

        try:
            self.instance = Client.objects.get(**query)
        except Client.DoesNotExist:
            self.instance = Client(**self.cleaned_data)

        if commit:
            self.instance.save()
        return self.instance


    class Meta:
        model = Client
        fields = ['name', 'bpn']


class CheckoutLocationForm(forms.ModelForm):
    def clean_building(self):
        building = self.cleaned_data['building']

        building = ' '.join(building.split())
        if building == building.lower():
            building = building.title()

        return building

    def clean_room(self):
        room = self.cleaned_data['room']

        room = ' '.join(room.split())
        # Remove leading zeros from any part of the room number
        room = ''.join([x[:-1].lstrip('0') + x[-1:] for x in re.split(r'(\d+)', room)])

        return room

    def save(self, commit=True):
        self.instance = super(CheckoutLocationForm, self).save(commit=False)

        try:
            self.instance = Location.objects.get(building__iexact=self.cleaned_data['building'], room__iexact=self.cleaned_data['room'])
        except Location.DoesNotExist:
            self.instance = Location(**self.cleaned_data)

        if commit:
            self.instance.save()
        return self.instance


    class Meta:
        model = Location
        exclude = []


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        exclude = []
