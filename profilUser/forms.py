from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['status', 'tanggal_lahir', 'description', 'foto_profil']
