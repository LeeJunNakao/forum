from django import forms
from django.template import loader
from django.forms.widgets import Widget
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator as PaginatorHandler

class TextArea(forms.Textarea):
    def __init__(self):
        super().__init__(attrs = {"class": "rounded border border-black focus:border-black w-full h-32 resize-none focus:[box-shadow:none]"})

class Pagination(Widget):
    template_name = 'widgets/pagination.html'

    def __init__(self, data, per_page = 10):
        super().__init__()
        self.pagination = PaginatorHandler(data, per_page)
    
    def get_page(self, page):
        return self.pagination.page(page)


    def get_context(self, current_page):
        page = self.pagination.page(current_page)

        return { 
            "current_page": current_page, 
            "total_pages": self.pagination.num_pages, 
            "has_next": page.has_next, 
            "has_previous": page.has_previous, 
            "next_page": page.next_page_number, 
            "previous_page": page.previous_page_number 
        } 

    def render(self, current_page):
        context = self.get_context(current_page=current_page)
        template = loader.get_template(self.template_name).render(context)

        return mark_safe(template)

class Input(forms.widgets.Input):
    def __init__(self, **kwargs):
        attrs = kwargs.get('attrs')
        rest_kwargs = { key: value for key, value in kwargs.items() if key != 'attrs'}
        super().__init__(attrs={"class": "rounded border border-blue-500 w-full p-2 focus:[box-shadow:none] focus:outline-none", **attrs}, **rest_kwargs)

class InputPassword(Input):
    def __init__(self, **kwargs):
        attrs = kwargs.get('attrs')
        rest_kwargs = { key: value for key, value in kwargs.items() if key != 'attrs'}
        super().__init__(attrs={**attrs, "type": "password"}, **rest_kwargs)

