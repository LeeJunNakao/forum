from django.template import loader
from django.forms.widgets import Widget
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator as PaginatorHandler

class SectionForm(Widget):
    template_name = 'widgets/forms/section_form.html'

    def render(self, title, form):
        template = loader.get_template(self.template_name).render({ "title": title, "form": form })

        return mark_safe(template)