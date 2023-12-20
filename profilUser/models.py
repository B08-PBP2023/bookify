from django.db import models
from django.contrib.auth.models import User

from pinjamBuku.models import Buku

class UserProfile(models.Model):
    
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    tanggal_lahir = models.CharField(null=True, blank=True, max_length=100)
    description = models.TextField(null=True, blank=True)

    
class Favorit(models.Model) :
    title = models.TextField(null=True, blank=True)
    id_book = models.IntegerField()
    authors = models.TextField(null=True, blank=True)
    language_code = models.TextField(null=True, blank=True)
    num_pages = models.IntegerField(null=True, blank=True)
    publication_date = models.TextField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)