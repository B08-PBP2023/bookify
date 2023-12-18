from django.urls import path
from profilUser import views
from profilUser.views import add_favorit, get_profilUser_json, show_page
from profilUser.views import show_page
from profilUser.views import edit_profil_ajax, get_favorites, delete_favorit, get_user_profile_by_name
from profilUser.views import add_favorit_flutter, get_favorite_by_user_flutter, delete_favorite_flutter,get_profile_flutter,edit_profile_flutter


app_name = 'profilUser'

urlpatterns = [
    path('', show_page, name='show_page'),
    path('get_product/', get_profilUser_json, name='get_profilUser_json'),
    path('edit_profil_ajax/', edit_profil_ajax, name='edit_profil_ajax'),
    path('add_favorit/<int:id_book>/', add_favorit, name='add_favorit'),
    path('get_favorites/', get_favorites, name='get_favorites'),
    path('get_user_profile_by_name/',get_user_profile_by_name, name='get_user_profile_by_name'),
    path('delete_favorit/<int:id>/', delete_favorit, name = 'delete_favorit'),
    
    path('get_profile_flutter/', get_profile_flutter, name='get_profile_flutter'),
    path('edit_profile_flutter/', edit_profile_flutter, name='edit_profile_flutter'),
    path('add_favorit_flutter/<int:book_id>/', add_favorit_flutter, name = 'add_favorit_flutter'),
    path('get_favorite_by_user_flutter/', get_favorite_by_user_flutter, name = 'get_favorite_by_user_flutter'),
    path('delete_favorite_flutter/<int:book_id>/', delete_favorite_flutter, name = 'delete_favorite_flutter'),

]


