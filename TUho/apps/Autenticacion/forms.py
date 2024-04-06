from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'type':"text",'name':"email", 'class':"input", 'required':'true', 'id': 'inputEmail'}),
    )

class ChangePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=("Contraseña"),
        widget=forms.PasswordInput(attrs={"class":"input", "name":"password1", "type":"password","required":"true"}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label=("Repetir Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class":"input", "name":"password2", "type":"password","required":"true"}),
    )

