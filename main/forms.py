from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegistrForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Логин'
    }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Пароль'
    }))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Повторите пароль'
    }))
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={
        'class': 'form-input',
        'placeholder': 'E-mail'
    }))
    nickname = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Никнейм'
    }))

    class Meta:
        model = User
        fields = ('nickname', 'username', 'email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")
        return password2


class LogForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Логин'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Пароль'
    }))
    
class PostForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'text-of-new-post',
        'placeholder': 'Ваш текст'
    }))
    image=forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'class': 'add-img-post',
        'style': 'background-color: #8270F2; width: 100%',
        'placeholder': 'Ваше изображение'
    }))