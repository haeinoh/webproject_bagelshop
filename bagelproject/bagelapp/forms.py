from django import forms
from .models import Suggestion

class SuggestionForm(forms.Form):
    suggestion = forms.CharField(
        label='Suggestion',
        max_length=140,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your suggestion',
            }))
