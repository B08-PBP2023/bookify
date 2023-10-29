from django import forms
from .models import BukuReq

# class BookRequestForm(forms.ModelForm):
#     class Meta:
#         model = BookRequest
#         fields = ['title', 'author', 'language_code', 'publication_date' ]

class BookRequestForm(forms.ModelForm):
    class Meta:
        model = BukuReq
        fields = ['title', 'authors', 'language_code','num_pages', 'publication_date','publisher']
        widgets = {
            'title': forms.TextInput(attrs={'type': 'text'}),  # Text input
            'authors': forms.TextInput(attrs={'type': 'text'}),  # Text input
            'language_code': forms.TextInput(attrs={'type': 'text'}),  # Text input
            'num_pages': forms.NumberInput(attrs={'type': 'number'}),  # Number input
            'publication_date': forms.DateInput(attrs={'type': 'date'}),  # Date input
            'publisher': forms.TextInput(attrs={'type': 'text'}),  # Text input for publisher
        }

        
