from django import forms
from rim.models import Group, Equipment

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude =[]

class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        exclude = ['latest_checkout']
