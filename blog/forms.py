from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    # tells Django which model we should use to create this form.
    class Meta:
        model = Post
        # the input fields will have title and post/text inputs
        fields = ("title", "text")

    #author is not included becausae it should be the user that is currently logged in.

