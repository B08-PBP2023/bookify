from django.urls import path, include
from requestBuku.views import show_home, book_request, get_books

app_name = 'requestBuku'
urlpatterns = [
    # path('', show_page, name='show_page'),
    # path('', views.home, name='home'),
    # path('book_request/', views.book_request, name='book_request'),
    path('', show_home, name= 'show_home'),
    path('book_request/', book_request, name= 'book_request'),
    path('get_books/', get_books, name = 'get_books'),

]