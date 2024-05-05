from django import forms

class TextArea(forms.Textarea):
    def __init__(self):
        super().__init__(attrs = {"class": "rounded border border-black focus:border-black w-full h-32 resize-none focus:[box-shadow:none]"})

class Input(forms.widgets.Input):
    def __init__(self, **kwargs):
        attrs = kwargs.get('attrs')
        rest_kwargs = { key: value for key, value in kwargs.items() if key != 'attrs'}
        super().__init__(attrs={"class": "rounded border border-blue-500 w-full p-2 focus:[box-shadow:none] focus:outline-none", **(attrs or dict())}, **rest_kwargs)

class InputPassword(Input):
    def __init__(self, **kwargs):
        attrs = kwargs.get('attrs')
        rest_kwargs = { key: value for key, value in kwargs.items() if key != 'attrs'}
        super().__init__(attrs={**(attrs or dict()), "type": "password"}, **rest_kwargs)

