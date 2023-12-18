from django.urls import path

# Create your views here.
from ulasanBuku.views import *
app_name = 'ulasanBuku'

urlpatterns = [

]

urlpatterns = [
    # path('', show_page, name='show_page'),
    path('get_books/', get_books, name = 'get_books'),
    # path('create_review/<int:book_id>/', create_review, name='create_review'),
    # path('create_review/', create_review, name='create_review'),
    path('review_list/<int:id>/', review_list, name='review_list'),
    path('', show_buku_ulasan, name='show_buku_ulasan'),
    
    # Mungkin Anda juga ingin menambahkan URL lain sesuai kebutuhan aplikasi Anda.
]