from django import forms
from .models import BukuReq

class BookRequestForm(forms.ModelForm):
    class Meta:
        model = BukuReq
        fields = ['title', 'authors', 'language_code','num_pages', 'publication_date','publisher']
        widgets = {
            'title': forms.TextInput(attrs={'type': 'text'}), 
            'authors': forms.TextInput(attrs={'type': 'text'}), 
            'language_code': forms.TextInput(attrs={'type': 'text'}), 
            'num_pages': forms.NumberInput(attrs={'type': 'number'}),  
            'publication_date': forms.DateInput(attrs={'type': 'date'}),  
            'publisher': forms.TextInput(attrs={'type': 'text'}),  
        }

        
