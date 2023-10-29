from django.contrib import admin
from .models import Buku
# Register your models here.
from pinjamBuku.models import Pinjaman


admin.site.register(Pinjaman)
admin.site.register(Buku)
