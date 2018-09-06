from django import forms
from rim.models import Group, Equipment

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude =[]

class AddForm(forms.ModelForm):

    class Meta:
        model = Equipment
        exclude = []
