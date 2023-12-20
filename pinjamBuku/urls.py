from django.urls import path
from pinjamBuku.views import *

app_name = 'pinjamBuku'

urlpatterns = [
    path('get_books/', get_books, name='get_books'),
    path('get_books_by_judul/<str:judul>/', get_books_by_judul, name='get_books_by_judul'),
    path('',show_page, name='show_page'),
    path('borrow-books/<int:id_book>/', borrow_books, name='borrow_books'),
    path('get_borrowed_books/', get_borrowed_books, name='get_borrowed_books'),
    path('delete_borrowed_books/<int:id>/', delete_borrowed_books, name = 'delete_borrowed_books'),
    path('show_borrow_books/', show_borrow_books, name='show_borrow_books'),
    path('borrow_books_flutter/<int:book_id>/', borrow_books_flutter, name = 'borrow_books_flutter'),
    path('get_books_by_user_flutter/', get_books_by_user_flutter, name = 'get_books_by_user_flutter'),
    path('delete_pinjaman_flutter/<int:book_id>/', delete_pinjaman_flutter, name = 'delete_pinjaman_flutter'),

    
]