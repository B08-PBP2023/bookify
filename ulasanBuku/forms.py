from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']

        widgets = {
            'rating': forms.Select(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
            'content': forms.Textarea(attrs={'rows': 4}),
        }
