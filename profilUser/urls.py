from django.urls import path
from profilUser.views import view_profile
from profilUser.views import view_profile, edit_profile
#from . import views

app_name = 'profilUser'

urlpatterns = [

    path('view-profile/', view_profile, name='view_profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    
    # Mungkin Anda juga ingin menambahkan URL lain sesuai kebutuhan aplikasi Anda.
]


