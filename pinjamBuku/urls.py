from django.urls import path
from pinjamBuku.views import get_books

app_name = 'pinjamBuku'

urlpatterns = [
    path('APIbooks/', get_books, name='get_books')
]