from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        fields = ('author', 'title', 'text')
        # Adding widget so that we cna gerab a aprticular filed widget and adjust css
        widgets= {
            'field' : forms.TextInput(attrs={'class': 'textinputclass'}),
            'text' : forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})

        }

class CommentForm(forms.ModelForm):
    
    class Meta():
        model = Comment
        fields = ("author", "text")
        widgets ={
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text' : forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
