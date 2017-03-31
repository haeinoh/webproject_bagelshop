from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class registration_form(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user=super(registration_form,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class SuggestionForm(forms.Form):
    suggestion = forms.CharField(
        label='Suggestion',
        max_length=140,
        widget=forms.TextInput(attrs={
            'placeholder': 'enter suggestion'
            }))

class blog_form(forms.Form):
    title = forms.CharField(
        label='Title',
        max_length=140,
        widget=forms.TextInput(attrs={
            'placeholder': 'enter title of blog post'
            }))
    content = forms.CharField(
        label='Title',
        widget=forms.Textarea(attrs={
            'placeholder': 'enter content of blog post'
            }))
    image=forms.ImageField(label="Image File")
    image_description=forms.CharField(label="Image Description", max_length=144)



class LoginForm(AuthenticationForm):
    username=forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name':'username'
        })
    )
    password=forms.CharField(
        label="Password",
        max_length=32,
        widget=forms.PasswordInput()
    )
