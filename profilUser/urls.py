from django.urls import path
from profilUser.views import show_page
from profilUser.views import show_page, create_profile
from profilUser.views import create_profile, edit_profile
#from . import views

app_name = 'profilUser'

urlpatterns = [
    path('', show_page, name='show_page'),
    path('create_profil/', create_profile, name='create_profil'),
    path('edit_profil/', edit_profile, name='edit_profil'),
    
    # Mungkin Anda juga ingin menambahkan URL lain sesuai kebutuhan aplikasi Anda.
]


