from django import forms
from .models import Post,Tag

class DateTimeInput(forms.DateTimeInput):
        input_type='datetime-local'

class blog_form(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["blog_tag","title","text","published_date"]
        widgets = {
            'published_date':DateTimeInput(),
        }

    blog_tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

class tag_form(forms.ModelForm):
     
     class Meta:
          model= Tag
          fields = ["tag_name"]
          