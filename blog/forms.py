from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

        widgets = {
        	'title' : forms.TextInput(attrs={'placeholder': '제목'}),
        	'text' : forms.Textarea(attrs={'placeholder': '내용'})
        }
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)