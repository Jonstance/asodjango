from django import forms
from .models import Comment, Sub


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')


class SubForm(forms.ModelForm):
    class Meta:
        model = Sub
        fields = ['email']