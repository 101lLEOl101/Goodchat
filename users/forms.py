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


class RegistrationForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Name'
            }
        ),
        # help_text='Enter First Name',
    )
    surname = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Surname'
            }
        ),
        # help_text='Enter Last Name',
    )
    login = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Login'
            }
        ),
        # help_text='Enter Username',
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Email'
            }
        ),
        # help_text='Enter Email Address',
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Password'
            }
        ),
    )
    re_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Repeat password'
            }
        ),
    )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     re_password = cleaned_data.get('re_password')
    #     if password != re_password:
    #         raise forms.ValidationError('Passwords are not equal')

    def clean_re_password(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']
        if password != re_password:
            raise forms.ValidationError('Passwords are not equal!')
        return re_password


class ProfileEditForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Name'
            }
        )
    )
    surname = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Surname'
            }
        )
    )
    avatar = forms.ImageField(
        upload_to="images/profile_avatars/",
        default="images/DEFAULT_AVATAR.png"
    )
    about = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'About'
            }
        )
    )
    country = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Country'
            }
        )
    )
    city = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'City'
            }
        )
    )
    education = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Education'
            }
        )
    )
    company = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Company'
            }
        )
    )
    hobby = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Hobby'
            }
        )
    )
