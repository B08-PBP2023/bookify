from django.db import models
from pinjamBuku.models import Buku
# Create your models here.

class Question(models.Model):
    isi_pertanyaan = models.TextField()
    judul_buku = models.TextField()
    # buku = models.ForeignKey(Buku, on_delete=models.CASCADE)

class QuestionAnswer(models.Model):
    isi_pertanyaan = models.TextField()
    isi_jawaban = models.TextField()
    judul_buku = models.TextField()
    # buku = models.ForeignKey(Buku, on_delete=models.CASCADE)