from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article # when we call form.save and so on it will be saved as a Product
        # Handle by ModelForm I assume?
        fields = [
            'title',
            'content',
            'active',
        ]