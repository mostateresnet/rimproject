from django import forms

from rim.models import Equipment

class AddForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ['serial_no', 'equipment_model', 'equipment_type', 'count']

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
