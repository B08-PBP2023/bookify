from django.urls import path
from .views import show_page, get_profilUser_json
from .views import get_wishlist,add_wishlist, delete_wishlist

app_name = "BacaDanWishlist"

urlpatterns = [
  path('', show_page, name='show_page'),
  path('get_product/', get_profilUser_json, name='get_profilUser_json'),
  path('get_wishlist/', get_wishlist, name='get_wishlist'),
  path('add_wishlist/<int:id>/', add_wishlist, name='add_wishlist'),
  path('delete_wishlist/<int:id>/', delete_wishlist, name='delete_wishlist'),
]