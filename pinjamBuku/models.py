from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Buku(models.Model):
    title = models.TextField(null=True, blank=True)
    authors = models.TextField(null=True, blank=True)
    language_code = models.TextField(null=True, blank=True)
    num_pages = models.IntegerField(null=True, blank=True)
    publication_date = models.TextField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)

class Pinjaman(models.Model) :
    title = models.TextField(null=True, blank=True)
    id_book = models.IntegerField()
    authors = models.TextField(null=True, blank=True)
    language_code = models.TextField(null=True, blank=True)
    num_pages = models.IntegerField(null=True, blank=True)
    publication_date = models.TextField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)