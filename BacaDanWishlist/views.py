from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from pinjamBuku.models import Buku
from profilUser.models import UserProfile
from .models import Wishlist
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
# Create your views here.

@login_required(login_url='/login')
def show_page(request):
  books = Buku.objects.all()
  context = {
    'name' : request.user.username,

    'books' : books,
  }
  return render(request, 'baca.html', context)

def get_profilUser_json(request):
  profil_user = UserProfile.objects.all()
  return HttpResponse(serializers.serialize('json', profil_user))

def get_wishlist(request):
  wishlist_books = Wishlist.objects.filter(user=request.user)

  print("Wishlist :", wishlist_books)
  return HttpResponse(serializers.serialize('json', wishlist_books))

@csrf_exempt
def delete_wishlist(request, id):
  if request.method == 'DELETE':
    data = Wishlist.objects.get(pk=id)
    data.delete()

    return HttpResponse(b"DELETE", status=201)
  
  return HttpResponseNotFound()

@csrf_exempt
def add_wishlist(request, id_book):
  print("TESTTTTT123123123")
  if request.method == 'POST' :
    buku = Buku.objects.get(pk=id_book)

    existing_wishlist = Wishlist.objects.filter(user=request.user, id_book=id_book).first()

    if existing_wishlist:
      #book with the same id_book already exists in Wishlist

      return HttpResponse("Book is already in wishlist", status=201)
    
    print(buku.title)
    print(type(id_book))

    new_item = Wishlist(user=request.user, id_book=id_book, title=buku.title, authors=buku.authors, Language_code=buku.language_code, num_pages=buku.num_pages, publication_date=buku.publication_date, publisher=buku.publisher)
    new_item.save()

    return HttpResponse(b"CREATED", status=201)
  
  return HttpResponseNotFound()
