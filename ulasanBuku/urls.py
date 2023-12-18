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
    path('add_ulasan_flutter/<int:id_book>/', add_ulasan_flutter, name='add_ulasan_flutter'),
    path('get_ulasan_filtered_json/<int:id_book>/', get_ulasan_filtered_json, name='get_ulasan_filtered_json'),
    
    # Mungkin Anda juga ingin menambahkan URL lain sesuai kebutuhan aplikasi Anda.
]