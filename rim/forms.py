from django import forms
from rim.models import Group, Equipment, Client

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude =[]

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        exclude = ['latest_checkout']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = []
