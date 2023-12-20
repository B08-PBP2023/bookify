from django import forms
from .models import Buku, Pinjaman

class BukuForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = ['role','tanggal_lahir', 'description']
