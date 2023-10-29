from django.urls import path
from Homepage.views import show_homepage, show_homepage_guest, show_list_of_books, get_books, show_list_of_books_guest

app_name = 'Homepage'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('guest/',show_homepage_guest, name='show_homepage_guest'),
    path('show_list_of_books/', show_list_of_books, name='show_list_of_books'),
    path('show_list_of_books_guest/', show_list_of_books_guest, name='show_list_of_books_guest'),
    path('get_books/', get_books, name='get_books'),

]