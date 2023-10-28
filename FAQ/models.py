from django.db import models
from pinjamBuku.models import Buku
# Create your models here.

class Question(models.Model):
    isi_pertanyaan = models.CharField(max_length=255)
    # id_buku = models.IntegerField()
    # judul_buku = models.TextField()
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)

class QuestionAnswer(models.Model):
    isi_pertanyaan = models.CharField(max_length=255)
    isi_jawaban = models.CharField(max_length=255)
    # id_buku = models.IntegerField()
    # judul_buku = models.TextField()
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)