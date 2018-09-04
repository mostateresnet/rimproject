from django import forms

from rim.models import Equipment

class AddForm(forms.ModelForm):

    class Meta:
        model = Equipment
<<<<<<< Updated upstream
        fields = ['serial_no', 'equipment_model', 'equipment_type', 'count']
=======
        fields = ['serial_no', 'equipment_model', 'equipment_type', 'count', 'manufacturer',
        'service_tag', 'smsu_tag', 'cpu', 'optical_drive', 'size', 'memory', 'other_connectivity',
        'hard_drive', 'usb_ports', 'video_card', 'removable_media', 'physical_address',
        'purchase_price', 'purchase_info']
>>>>>>> Stashed changes

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
