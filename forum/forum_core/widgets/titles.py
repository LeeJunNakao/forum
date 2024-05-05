from django.template import loader
from django.forms.widgets import Widget
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator as PaginatorHandler

class PageTitle(Widget):
    def render(self, text):
        return mark_safe(f'<h1 class="font-medium text-3xl text-blue-600">{text}</h2>')
    
class SectionTitle(Widget):
    def render(self, text):
        return mark_safe(f'<h2 class="font-medium text-xl text-blue-400">{text}</h2>')