from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    tanggal_lahir = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    foto_profil = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
