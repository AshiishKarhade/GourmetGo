from django import forms
from .models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean(self):
        cleaned_date = super(UserForm, self).clean()
        password = cleaned_date.get('password')
        confirm_password = cleaned_date.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords does not match!")
