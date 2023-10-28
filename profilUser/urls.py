from django.urls import path
from profilUser import views
from profilUser.views import get_profilUser_json, show_buku, show_page
from profilUser.views import show_page, create_profil
from profilUser.views import create_profil
from profilUser.views import create_profil, edit_profil_ajax
#from . import views

app_name = 'profilUser'

urlpatterns = [
    path('', show_page, name='show_page'),
    path('create_profil/', create_profil, name='create_profil'),
    path('', show_buku, name = 'show_buku'),
    path('get_product/', get_profilUser_json, name='get_profilUser_json'),
    path('edit_profil_ajax/', edit_profil_ajax, name='edit_profil_ajax'),
    path('profilUser/show_page/<int:book_pk>/', views.show_page, name='show_page'),
]


