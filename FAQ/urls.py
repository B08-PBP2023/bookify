from django.urls import path
from FAQ.views import show_page

app_name = 'FAQ'

urlpatterns = [
    path('', show_page, name = 'show_page'),

]