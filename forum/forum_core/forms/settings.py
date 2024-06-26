from forum_core.widgets.inputs import Input, InputPassword, ImageUploadInput
from django import forms
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    avatar = forms.FileField(widget=ImageUploadInput('avatar'), label='',required=False)
    first_name = forms.CharField(widget=Input(), label='First name')
    last_name = forms.CharField(widget=Input(), label="Last name")
    email = forms.CharField(widget=Input(), label="Email")

    def set_avatar(self, avatar_url):
        self.fields['avatar'].widget.set_image_src(avatar_url)

    
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