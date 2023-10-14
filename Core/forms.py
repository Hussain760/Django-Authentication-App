from typing import Any
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from django.contrib.auth.models import User
from django import forms


class SignInForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control bg-dark text-light"}),
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control bg-dark text-light"}),
    )
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control bg-dark text-light"}),
    )
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={"class": "form-control bg-dark text-light"}),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control bg-dark text-light"}),
        label="Password",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control bg-dark text-light"}),
        label="Repeat Password",
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if User.objects.filter(username=username).exists():
            self.add_error("username", "Username is already taken.")

        if User.objects.filter(email=email).exists():
            self.add_error("email", "Email is already in use.")

        return cleaned_data


class UpdateForm(UserChangeForm):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control bg-dark text-light"}),
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control bg-dark text-light"}),
    )
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control bg-dark text-light"}),
    )
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={"class": "form-control bg-dark text-light"}),
    )
    password = forms.Field(
        help_text="<a href='changepassword/' class='text-light'>Change Your Password</a>"
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        )

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if User.objects.filter(username=username).exclude(id=self.instance.id).exists():
            self.add_error("username", "Username is already taken.")

        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error("email", "Email is already in use.")

        return cleaned_data


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control bg-dark text-light"})
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control bg-dark text-light"}),
        label="New Password",
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control bg-dark text-light"}),
        label="Confirm Password",
    )

    class Meta:
        model = User
        fields = (
            "old_password",
            "new_password1",
            "new_password2",
        )
