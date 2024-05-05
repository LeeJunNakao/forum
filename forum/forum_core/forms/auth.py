from forum_core.widgets.inputs import  Input, InputPassword
from forum_core.models.topic import User
from django import forms

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField(widget=Input(attrs={"placeholder": "Username"}), label='')
    password = forms.CharField(widget=InputPassword(attrs={"placeholder": "Password"}), label='')
