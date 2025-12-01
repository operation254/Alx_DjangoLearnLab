from django import forms
from .models import Book


class ExampleForm(forms.ModelForm):
    """
    Simple example form used in the security project.
    """
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]
