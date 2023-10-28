from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from pinjamBuku.models import Buku
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

def show_page(request):
    books = Buku.objects.all()
    context = {
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
