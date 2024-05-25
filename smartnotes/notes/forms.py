from django import forms
from django.core.exceptions import ValidationError
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model= Notes
        fields = ('title','content')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control my-5'}),
            'content': forms.Textarea(attrs={'class':'form-control my-5'})
        }
        labels = {
            'content':'write what you want'
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError("We only concern title with Django")
        return title