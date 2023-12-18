from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.core import serializers
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm  # Anda perlu membuat form terlebih dahulu
from pinjamBuku.models import Buku
from django.http import HttpResponseNotFound, HttpResponse

import json

@login_required

def show_page(request):
    books = Buku.objects.all()
    context = {
        'books':books,
    }
    return render(request, 'show_buku_ulasan.html', context)

def review_list(request, id):
    books = Buku.objects.all()
    book = Buku.objects.get(pk=id)
    form = ReviewForm(request.POST or None)
    if(form.is_valid() and request.method=="POST"):
        item = form.save(commit=False)
        item.user = request.user
        item.book = Buku.objects.get(pk=id)
        item.save()

        reviews = Review.objects.filter(user=request.user, book=book)

        context = {
            'reviews' : reviews,
            'books' : books,
        }

        return render(request, 'ulasan_page.html', context)


    reviews = Review.objects.filter(book=book)

    context = {
        'reviews' : reviews,
        'books' : books,
    }
    return render(request, 'ulasan_page.html', context)

def get_books(request):
    books = Buku.objects.all()
    return HttpResponse(serializers.serialize('json',books))

def show_buku_ulasan(request):

    books = Buku.objects.all()

    context = {
        'books':books,
    }

    return render(request, 'show_buku_ulasan2.html', context)

def add_ulasan(request, id_book):
    if request.method == 'POST':
        buku = Buku.objects.get(pk=id_book)

        judul_buku = buku.title
        isi_ulasan = request.POST.get("isi_ulasan")

        new_item = Review(isi_ulasan=isi_ulasan, buku=buku)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def add_ulasan_flutter(request, id_book):
    if request.method == 'POST':
        book = Buku.objects.get(pk=id_book)
        data = json.loads(request.body)
        isi_ulasan = data["isi_ulasan"]

        new_item = Review(isi_ulasan=isi_ulasan, book=book)
        new_item.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
def get_ulasan_filtered_json(request, id):
    book = Buku.objects.get(pk=id)
    judul_book = book.title
    
    isi_ulasan = Review.objects.filter(book = book)
    
    return HttpResponse(serializers.serialize('json', isi_ulasan))