from django import forms
from tms.models import Target, Note

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