from django.urls import path
from Homepage.views import show_homepage

app_name = 'Homepage'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
]