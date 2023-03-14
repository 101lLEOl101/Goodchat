from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Username',
            }
        )
    )
    password = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Password',
            }
        )
    )
