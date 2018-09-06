from django import forms

from rim.models import Equipment

class AddForm(forms.ModelForm):

    class Meta:
        model = Equipment
        exclude = []
