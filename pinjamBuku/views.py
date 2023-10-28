from django.shortcuts import render

from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from pinjamBuku.models import Buku
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@login_required  # Ensure the user is logged in to borrow a book

def get_books(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("json",data), content_type='application/json')

def show_page(request):
    context = {

    }
    return render(request, "catalog.html", context)

@csrf_exempt
def borrow_books(request, id_book):
    if request.method == 'POST':
        buku = Buku.objects.get(pk=id_book)
        
        borrowed_books = Buku.objects.filter(user=request.user, id_book=id_book).first()

        if borrowed_books:
            # Book with the same id_book already exists in Favorit
            
            return HttpResponse("Book is already in borrowed book list", status=201)
        
        print(buku.title)
        print(type(id_book))
        
    
        new_item = Buku(user=request.user, id_book=id_book, title=buku.title, authors=buku.authors, language_code=buku.language_code, num_pages=buku.num_pages, publication_date=buku.publication_date, publisher=buku.publisher)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()