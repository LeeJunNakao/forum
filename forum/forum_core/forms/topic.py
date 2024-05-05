from forum_core.widgets.inputs import TextArea, Input
from forum_core.models.topic import Reply, Topic
from django import forms

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']

    content = forms.CharField(widget=TextArea(), label='')

class CreateTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description']
    
    title = forms.CharField(widget=Input(attrs={"placeholder": "Title"}), label='')
    description = forms.CharField(widget=TextArea(), label='')