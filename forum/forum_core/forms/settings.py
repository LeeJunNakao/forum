from forum_core.widgets.inputs import Input, InputPassword
from django import forms
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    first_name = forms.CharField(widget=Input())
    last_name = forms.CharField(widget=Input())
    email = forms.CharField(widget=Input())

    
class PasswordlForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']

    password = forms.CharField(widget=InputPassword())
    repeat_password = forms.CharField(widget=InputPassword())

    def check_password_confirmation(self):
        password = self['password'].value()
        repeat_password = self['repeat_password'].value()
        
        return password == repeat_password