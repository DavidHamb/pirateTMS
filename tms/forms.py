from django import forms
from tms.models import Target

STYLE_PARAMETERS = 'width: 500px; padding: 10px 30px; font-size: 16px;'

class TargetForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Name',
                }),
            'description': forms.TextInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Description',
                }),                
            'ip': forms.TextInput(attrs={
                'class': "form-control", 
                'style': STYLE_PARAMETERS,
                'placeholder': 'IP Address'
                }),
            'hostname': forms.TextInput(attrs={
                'class': "form-control", 
                'style': STYLE_PARAMETERS,
                'placeholder': 'Hostname'
                }),
            'url': forms.TextInput(attrs={
                'class': "form-control", 
                'style': STYLE_PARAMETERS,
                'placeholder': 'URL'
                })
        }