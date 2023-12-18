from django.db import models
from django.contrib.auth.models import User
from pinjamBuku.models import Buku

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Buku, on_delete=models.CASCADE)  # Menambahkan foreign key ke model Buku
    rating = models.PositiveIntegerField(default=0)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

