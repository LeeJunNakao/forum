from django import forms
from django.template import loader
from django.forms.widgets import Widget
from django.utils.safestring import mark_safe

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

class ImageUploadInput(Widget):
    template_name = 'widgets/inputs/image-upload-input.html'
    
    def __init__(self, attr_name, attr_id = None, **kwargs):
        super().__init__(**kwargs)
        self.attr_name = attr_name
        self.attr_id = attr_id or attr_name
    
    def get_context(self):
        return {"input_name": self.attr_name, "input_id": self.attr_id}

    def render(self, *args, **kwargs):

        context = self.get_context()
        template = loader.get_template(self.template_name).render(context)

        return mark_safe(template)