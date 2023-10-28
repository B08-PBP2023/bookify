from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from pinjamBuku.models import Buku
from .models import Favorit, UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

@login_required(login_url='/login')
def show_page(request):
    books = Buku.objects.all()
    context = {
        'name': request.user.username,
      
        'books':books,
    }
    return render(request, 'profil.html', context)

def show_buku(request):

    books = Buku.objects.all()

    context = {
        'books':books,
    }

    return render(request, 'show_buku.html', context)

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'userprofile/profil.html', {'user_profile': user_profile})

@login_required
def create_profil(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = UserProfileForm()
    return render(request, 'userprofile/create_profil.html', {'form': form})

@csrf_exempt
def edit_profil_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        status = request.POST.get("status")
        tanggal_lahir = request.POST.get("tanggal_lahir")
        description = request.POST.get("description")
        foto_profil = request.POST.get("foto_profil")


        user_profile = UserProfile.objects.get(user=request.user)

        user_profile.name = name
        user_profile.status = status
        user_profile.tanggal_lahir = tanggal_lahir
        user_profile.description = description
        user_profile.foto_profil = foto_profil
        user_profile.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_profilUser_json(request):
    profil_user = UserProfile.objects.all()
    return HttpResponse(serializers.serialize('json', profil_user))

def get_favorites(request):
    # book = Buku.objects.get(pk=id)
    
    favorite_books = Favorit.objects.filter(user=request.user)
    
    print("Favoriteee: ", favorite_books)
    return HttpResponse(serializers.serialize('json', favorite_books))
    

@csrf_exempt
def delete_favorit(request,id):
    if request.method == 'DELETE':
        data = Favorit.objects.get(pk=id)
        data.delete()

        return HttpResponse(b"DELETE", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def add_favorit(request, id_book):
    print("TESTTTTTTTTTTTTTTTTTTT")
    if request.method == 'POST':
        buku = Buku.objects.get(pk=id_book)
        
        existing_favorit = Favorit.objects.filter(user=request.user, id_book=id_book).first()

        if existing_favorit:
            # Book with the same id_book already exists in Favorit
            
            return HttpResponse("Book is already in favorite list", status=201)
        
        print(buku.title)
        print(type(id_book))
        
        # title = models.TextField(null=True, blank=True)
        # authors = models.TextField(null=True, blank=True)
        # language_code = models.TextField(null=True, blank=True)
        # num_pages = models.IntegerField(null=True, blank=True)
        # publication_date = models.TextField(null=True, blank=True)
        # publisher = models.TextField(null=True, blank=True)
    
        new_item = Favorit(user=request.user, id_book=id_book, title=buku.title, authors=buku.authors, language_code=buku.language_code, num_pages=buku.num_pages, publication_date=buku.publication_date, publisher=buku.publisher)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()