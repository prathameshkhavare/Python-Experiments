import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not re.fullmatch(r"[A-Za-z0-9_]{3,30}", username):
            raise forms.ValidationError("Use 3 to 30 letters, numbers, or underscores.")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if not re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email):
            raise forms.ValidationError("Enter a valid email address.")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email
