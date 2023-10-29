from django.db import models
from django.contrib.auth.models import User

class BukuReq(models.Model):
    title = models.TextField(null=True, blank=True)
    authors = models.TextField(null=True, blank=True)
    language_code = models.TextField(null=True, blank=True)
    num_pages = models.IntegerField(null=True, blank=True)
    publication_date = models.TextField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)

# class BookRequest(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     request_date = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     language_code = models.CharField(max_length= 100)
#     publication_date = models.DateField()