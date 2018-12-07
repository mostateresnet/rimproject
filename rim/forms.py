from django import forms
from rim.models import Equipment


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        exclude = ['latest_checkout']
