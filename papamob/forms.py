from django import forms
from .models import PPost, CComment, Images

class PostForm(forms.ModelForm):

    class Meta:
        model = PPost
        fields = ('title', 'text')

        widgets = {
            'title' : forms.TextInput(attrs={'placeholder': '제목'}),
            'text' : forms.Textarea(attrs={'placeholder': '내용'}),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = CComment
        fields = ('author', 'text',)

        widgets = {
            'author' : forms.TextInput(attrs={'placeholder': '이름'}),
            'text' : forms.Textarea(attrs={'placeholder': '내용'})
        }
