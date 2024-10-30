from django import forms
from tms.models import Target, Note, Vulnerability, Ressource

STYLE_PARAMETERS = 'width: 500px; padding: 10px 30px; font-size: 16px;'
PICKLIST_STYLE_PARAMETERS = 'width: 500px; padding: 10px 30px; font-size: 16px; background-color: #cceeff'

class TargetForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = ['name', 'ip', 'hostname', 'url', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Name',
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
                }),
            'description': forms.Textarea(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Description',
                })
        }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Title',
                }),
            'content': forms.Textarea(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Write your note ...',
                }),
        }


class VulnerabilityForm(forms.ModelForm):
    class Meta:
        model = Vulnerability
        fields = ['name', 'url', 'category', 'cve', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Name',
                }),
            'description': forms.Textarea(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Description',
                }),   
            'category': forms.Select(attrs={
                'class': "form-control", 
                'style': PICKLIST_STYLE_PARAMETERS,
                }),
            'url': forms.URLInput(attrs={
                'class': "form-control", 
                'style': STYLE_PARAMETERS,
                'placeholder': 'URL'
                }),
            'cve': forms.TextInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'CVE-XXXX-XXXXXX'
            })
        }


class RessourceForm(forms.ModelForm):
    class Meta:
        model = Ressource
        fields = ['name', 'url', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Name',
                }),                
            'url': forms.TextInput(attrs={
                'class': "form-control", 
                'style': STYLE_PARAMETERS,
                'placeholder': 'URL'
                }),
            'description': forms.Textarea(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Description',
                })
        }