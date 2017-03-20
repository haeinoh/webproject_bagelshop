from django import forms
from .models import *
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

class menu_form(forms.Form):
    title=forms.CharField(label="Title",max_length=144)
    content=forms.CharField(label="Blog Content",widget=forms.Textarea)
    image=forms.ImageField(label="Image File")
    image_description=forms.CharField(label="Image Description", max_length=144)

    def save(self, request , commit=True):
        menu = Blog()
        menu.title=self.cleaned_data['title']
        menu.content=self.cleaned_data['content']
        menu.image=self.cleaned_data['image']
        menu.image_description=self.cleaned_data['image_description']
        menu.author=request.user
        if commit:
            menu.save()
        return blog
