from django.shortcuts import redirect, render

from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .models import Buku, Pinjaman
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404



# Create your views here.
def get_books(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("json",data), content_type='application/json')

def get_books_by_judul(request, judul):
    data = Buku.objects.filter(title__icontains=judul)
    return HttpResponse(serializers.serialize("json",data), content_type='application/json')

def show_page(request):
    context = {

    }
    return render(request, "catalog.html", context)

def show_borrow_books(request):
    print("DIRECTT")
    context = {

    }
    return render(request, "borrowed_books.html", context)


def get_borrowed_books(request):    
    borrowed_books = Pinjaman.objects.filter(user=request.user)
    print("Borrowed: ", borrowed_books)
    return HttpResponse(serializers.serialize('json', borrowed_books))
    

@csrf_exempt
def delete_borrowed_books(request,id):
    print("KEMBALIKANNN")
    if request.method == 'DELETE':
        data = Pinjaman.objects.get(id_book=id)
        data.delete()

        return HttpResponse(b"DELETE", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def borrow_books(request, id_book):
    print("TESTTTTTTTTTTTTTTTTTTT")
    buku = Buku.objects.get(pk=id_book)
    
    existing_borrowed = Pinjaman.objects.filter( id_book=id_book).first()

    if existing_borrowed:
        print("YAAAAAAAAAAA")
        return HttpResponseNotFound()
    
    new_item = Pinjaman( user=request.user, id_book=buku.pk, title=buku.title, authors=buku.authors, language_code=buku.language_code, num_pages=buku.num_pages, publication_date=buku.publication_date, publisher=buku.publisher)
    new_item.save()
    return HttpResponse(b"DELETE", status=201)
    



@csrf_exempt
@login_required(login_url='/auth/login')
def borrow_books_flutter(request, book_id):
    if request.method == 'POST':
        user = request.user
        try:
            buku = Buku.objects.get(pk=book_id)
            if not Pinjaman.objects.filter(user=user, id_book=buku.pk).exists():
                pinjaman = Pinjaman(user=user, id_book=buku.pk, title = buku.title, authors = buku.authors, language_code = buku.language_code,
                                   num_pages = buku.num_pages, publication_date = buku.publication_date,publisher = buku.publisher)
                pinjaman.save()
                return JsonResponse({'status' : 'success', 'msg': 'Add to pinjaman successfully'}, status=200)
            else:
                return JsonResponse({'status' : 'failed', 'msg': 'Book is already pinjamand'}, status=400)
        except Buku.DoesNotExist:
            return JsonResponse({'status' : 'failed', 'msg': 'Book not found'}, status=400)
    return JsonResponse({'status' : 'failed', 'msg': 'Invalid request'}, status=400)

@login_required
def get_books_by_user_flutter(request):
    user = request.user

    print(user.username)
    pinjaman = Pinjaman.objects.filter(user = user).all()
    user_pinjaman = []
    for buku in pinjaman:
        user_pinjaman.append({
            'user_id' : buku.user.pk,
            'id_book' : buku.id_book,
            'authors' : buku.authors,
            'title' : buku.title,
            'language_code' : buku.language_code,
            'num_pages' : buku.num_pages,
            'publication_date' : buku.publication_date,
            'publisher' : buku.publisher,
        })
    return JsonResponse({'status' : 'success','data' : user_pinjaman} , content_type="application/json")

@csrf_exempt
@login_required(login_url='/auth/login')
def delete_pinjaman_flutter(request, book_id):
    if request.method == 'POST':
        user = request.user
        try:
            buku = Buku.objects.get(pk=book_id)
            pinjaman = Pinjaman.objects.filter(user=user, id_book=buku.pk).first()
            if pinjaman:
                pinjaman.delete()
                return JsonResponse({'status' : 'success','msg': 'Removed from pinjaman successfully'}, status=200)
            else:
                return JsonResponse({'status' : 'failed', 'msg': 'Book is not pinjamand'}, status=400)
        except Buku.DoesNotExist:
            return JsonResponse({'status' : 'failed', 'msg': 'Book not found'}, status=400)
    return JsonResponse({'status' : 'failed', 'msg': 'Invalid request'}, status=400)