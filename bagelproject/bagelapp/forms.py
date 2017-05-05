from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *

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

class product_form(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=140,
        widget=forms.TextInput(attrs={
            'placeholder': 'enter name of product'
            }))
    price = forms.IntegerField(label="price",label_suffix='$')
    image=forms.ImageField(label="Image")
    description=forms.CharField(label="Image Description", max_length=144)

class custom_form(forms.Form):
    title = forms.CharField(
        label='Title',
        max_length=140,
        widget=forms.TextInput(attrs={
            'placeholder': 'enter title of your recipe'
            }))
    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(attrs={
            'placeholder': 'enter content of your recipe'
            }))
    image=forms.ImageField(label="Image File")
    
    def save(self, request, commit=True):
        custom = Custom()
        custom.title=self.cleaned_data["title"]
        custom.content=self.cleaned_data["content"]
        custom.image=self.cleaned_data["image"]
        custom.author=request.user
        if commit:
            custom.save()
        return custom

class order_form(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=140,
        widget=forms.TextInput(attrs={
            'placeholder': 'enter name of product'
            }))
    price = forms.IntegerField(label="price",label_suffix='$')
    image=forms.ImageField(label="Image")
    description=forms.CharField(label="Image Description", max_length=144)

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
