from django import forms
from .models import Buku

# class BookRequestForm(forms.ModelForm):
#     class Meta:
#         model = BookRequest
#         fields = ['title', 'author', 'language_code', 'publication_date' ]

class BookRequestForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = ['title', 'authors', 'language_code', 'publication_date']

    title_input = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    author_input = forms.CharField(
        label='Author',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    language_code_input = forms.CharField(
        label='Language Code',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    publication_date_input = forms.DateField(
        label='Publication Date',
        widget=forms.DateInput(attrs={'class': 'form-control'}),
    )