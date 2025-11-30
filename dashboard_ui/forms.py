from django import forms
from Smart_Load_Health_Monitor.models import Appliance

class ApplianceForm(forms.ModelForm):
    class Meta:
        model = Appliance
        fields = [
            'appliance',
            'model',
            'serial',
            'location',
            'service_date',
            'kit',
            'service_repeat',
        ]
        widgets = {
            'service_date': forms.DateInput(attrs={'type': 'date'})
        }