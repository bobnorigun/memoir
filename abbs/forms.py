from django import forms
from .models import PapaAbb

class PostForm(forms.ModelForm):

    class Meta:
        model = PapaAbb
        fields = ('releasenote',)

        widgets = {
            'releasenote' : forms.Textarea(attrs={'placeholder': '릴리즈노트'})
        }
