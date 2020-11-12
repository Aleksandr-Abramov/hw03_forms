from django import forms
from django.forms import ModelForm

from .models import Group
from .models import Post

#Максим, здравствуйте. Сохранил старый вариант создания формы в комментариях. Как напоминание. Прошу, не осуждать.)
# class PostForm(forms.Form):
#     group = forms.ModelChoiceField(queryset=Group.objects.all(),
#                                    label="Группа",
#                                    required=False
#                                    )
#     text = forms.CharField(widget=forms.Textarea)

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["group", "text"]
        widgets = {
            "text": forms.Textarea()
        }
