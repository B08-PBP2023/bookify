from django.urls import path
from requestBuku.views import show_home, book_request, get_books, delete_request

app_name = 'requestBuku'
urlpatterns = [
    path('', show_home, name= 'show_home'),
    path('book_request/', book_request, name= 'book_request'),
    path('get_books/', get_books, name = 'get_books'),
    path('delete/<int:id>', delete_request, name='delete_request'),
]