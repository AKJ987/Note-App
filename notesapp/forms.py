from django import forms
from notesapp.models import NotesModel

class NotesForm(forms.ModelForm):
    class Meta:
        model=NotesModel
        fields='__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Title'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Enter your note'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

