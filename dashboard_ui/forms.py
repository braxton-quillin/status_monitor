from django import forms
from .models import Appliance

class ApplianceForm(forms.ModelForm):
    class Meta:
        model = Appliance
        fields = [
            'name',
            'model_number',
            'serial_number',
            'location',
            'service_date',
            'kit',
        ]
        widgets = {
            'manufacture_date': forms.DateInput(attrs={'type': 'date'})
        }