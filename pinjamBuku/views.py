from django.shortcuts import redirect, render

from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.contrib.auth.decorators import login_required
from pinjamBuku.models import Buku, Pinjaman
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404



# Create your views here.
@login_required  # Ensure the user is logged in to borrow a book

def get_books(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("json",data), content_type='application/json')

def show_page(request):
    context = {

    }
    return render(request, "catalog.html", context)

def show_borrow_books(request):
    context = {

    }
    return render(request, "borrowed_books.html", context)


def get_borrowed_books(request):    
    borrowed_books = Pinjaman.objects.filter(user=request.user)
    print("Borrowed: ", borrowed_books)
    return HttpResponse(serializers.serialize('json', borrowed_books))
    

@csrf_exempt
def delete_borrowed_books(request,id):
    if request.method == 'DELETE':
        data = Pinjaman.objects.get(pk=id)
        data.delete()

        return HttpResponse(b"DELETE", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def borrow_books(request, id_book):
    print("TESTTTTTTTTTTTTTTTTTTT")
    buku = Buku.objects.get(pk=id_book)
    
    existing_borrowed = Pinjaman.objects.filter( id=id_book).first()

    if existing_borrowed:
        new_item = Pinjaman( user=request.user, id_book=buku.pk, title=buku.title, authors=buku.authors, language_code=buku.language_code, num_pages=buku.num_pages, publication_date=buku.publication_date, publisher=buku.publisher)
        new_item.save()
        return redirect('pinjamBuku:show_borrow_books')
    
    print(buku.title)
    print(type(id_book))
        
        # title = models.TextField(null=True, blank=True)
        # authors = models.TextField(null=True, blank=True)
        # language_code = models.TextField(null=True, blank=True)
        # num_pages = models.IntegerField(null=True, blank=True)
        # publication_date = models.TextField(null=True, blank=True)
        # publisher = models.TextField(null=True, blank=True)
    



    return HttpResponseNotFound()

