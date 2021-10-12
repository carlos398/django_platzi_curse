"""User forms."""

# Django
from django import forms

# models
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """Sign up form"""

    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(max_length=70, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput)

    firs_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput)

    def clean_username(self):
        """username must be unique"""
        username = self.cleaned_data['username']
        username_in_use = User.objects.filter(username=username).exists()
        if username_in_use:
            raise forms.ValidationError('username is already in use')
        return username


    def clean(self):
        """Verify password confirmation match """
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('passwprds do not match')

        return data


    def safe(self):
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objets.create_user(**data)
        profile = Profile(user=user)
        profile.save()

class ProfileForm(forms.Form):
    """Profile form."""

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()