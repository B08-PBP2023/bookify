from django.urls import path
from pinjamBuku.views import get_books, show_page, borrow_books

app_name = 'pinjamBuku'

urlpatterns = [
    path('get_books/', get_books, name='get_books'),
    path('',show_page, name='show_page'),
    path('borrow_books/<int:id_book>/', borrow_books, name='borrow_books'),
]