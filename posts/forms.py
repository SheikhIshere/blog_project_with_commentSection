from django import forms
from .models import Post
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['name', 'email', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']  # Only show body field in the form        