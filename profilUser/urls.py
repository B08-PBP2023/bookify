from django.urls import path
from profilUser import views
from profilUser.views import add_favorit, get_profilUser_json, show_buku, show_page
from profilUser.views import show_page, create_profil
from profilUser.views import create_profil
from profilUser.views import create_profil, edit_profil_ajax, get_favorites, delete_favorit, get_user_profile_by_name
#from . import views

app_name = 'profilUser'

urlpatterns = [
    path('', show_page, name='show_page'),
    path('create_profil/', create_profil, name='create_profil'),
    # path('', show_buku, name = 'show_buku'),
    path('get_product/', get_profilUser_json, name='get_profilUser_json'),
    path('edit_profil_ajax/', edit_profil_ajax, name='edit_profil_ajax'),
    path('add_favorit/<int:id_book>/', add_favorit, name='add_favorit'),
    path('get_favorites/', get_favorites, name='get_favorites'),
    path('get_user_profile_by_name/',get_user_profile_by_name, name='get_user_profile_by_name'),
    path('delete_favorit/<int:id>/', delete_favorit, name = 'delete_favorit'),
]


