from forum_core.widgets import TextArea
from forum_core.models import Reply
from django import forms

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']

    content = forms.CharField(widget=TextArea(), label='')
