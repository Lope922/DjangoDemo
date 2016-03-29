from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    # tells Django which model we should use to creat this form.
    class Meta:
        model = Post
        fields = ("title", "text")

    #author is not included becausae it should

