from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Account


class ExtendedUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)


        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ("genres", "schedule", "time", "gameStyle")


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username",)


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ("genres", "schedule", "time", "gameStyle")
        widgets = {
            "time": forms.Select(attrs={"class": "select"}),
            "gameStyle": forms.Select(attrs={"class": "select"}),
            "genres": forms.CheckboxSelectMultiple(attrs={"class": "choice"}),
            "schedule": forms.CheckboxSelectMultiple(attrs={"class": "choice"}),
        }
