from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse, QueryDict
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from authentication.models import UserWithRole
from pinjamBuku.models import Buku
from .models import Favorit, UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json


@login_required(login_url='/login')
def show_page(request):
    books = Buku.objects.all()
    user_with_role = UserWithRole.objects.get(user=request.user)
    role = user_with_role.role

    context = {
        'name': request.user.username,
        'role': role,
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


@csrf_exempt
def edit_profil_ajax(request):
    if request.method == 'POST':
        tl = request.POST.get('tanggal_lahir')

        if is_valid_date(tl)==False:
            return HttpResponseNotFound(404)
        
        
        desc = request.POST.get('description')
        
        name = request.user.username
        try:
            user_profile = UserProfile.objects.get(name=name)
            user_profile.delete()
        except:
            print('Gak ada')
        
        try:
            user_with_role = UserWithRole.objects.get(user=request.user)
        except:
            return HttpResponseRedirect(reverse('authentication:login'))
        role = user_with_role.role

        new_item = UserProfile(name=name, role=role, tanggal_lahir=tl, description=desc)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_profilUser_json(request):
    profil_user = UserProfile.objects.all()
    return HttpResponse(serializers.serialize('json', profil_user))

def get_user_profile_by_name(request):
    name = request.user.username
    try:
        user_profile = UserProfile.objects.get(name=name)
        print("UDAH ADAA")
        user_profile = [user_profile]
        return HttpResponse(serializers.serialize('json', user_profile))
    except:
        user_with_role = UserWithRole.objects.get(user=request.user)
        role = user_with_role.role
        user_profile = UserProfile(name=name, role=role, tanggal_lahir="", description="")
        user_profile.save()
        user_profile = [user_profile]
        print("BIKIN USER PROFILE BARU")
        return HttpResponse(serializers.serialize('json', user_profile))


def get_favorites(request):
    
    favorite_books = Favorit.objects.filter(user=request.user)
    
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

    if request.method == 'POST':
        buku = Buku.objects.get(pk=id_book)
        
        existing_favorit = Favorit.objects.filter(user=request.user, id_book=id_book).first()

        if existing_favorit:
            # Book with the same id_book already exists in Favorit
            
            return HttpResponse("Book is already in favorite list", status=201)
        
        print(buku.title)
        print(type(id_book))
    
        new_item = Favorit(user=request.user, id_book=id_book, title=buku.title, authors=buku.authors, language_code=buku.language_code, num_pages=buku.num_pages, publication_date=buku.publication_date, publisher=buku.publisher)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


def is_valid_date(date_string):
    date_format = "%d/%m/%Y"
    try:
        # Attempt to parse the date using the provided format
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        # If parsing fails, it's not a valid date
        return False


@login_required(login_url='/auth/login')
def get_profile_flutter(request):
    try:
        user = request.user
        
        user_profile = UserProfile.objects.get(name=user.username)
        user_data = {
            "username": user_profile.name,
            "role": user_profile.role,
            "tanggalLahir": user_profile.tanggal_lahir,
            "description": user_profile.description,
        }
        print (user_data)
        return JsonResponse({"status": "success", "data": user_data}, status=200)
    except UserProfile.DoesNotExist:
        return JsonResponse({"status": "error", 'msg': 'User tidak ditemukan'}, status=404)
    except Exception as e:
        return JsonResponse({"status": "error", 'msg': str(e)}, status=500)

@csrf_exempt
@login_required(login_url='/auth/login')
def edit_profile_flutter(request):
    try:
        user = request.user
        user_profile = UserProfile.objects.get(name=user.username)
        print ("mantap", user_profile.tanggal_lahir)
        if request.method == 'POST':
            data = QueryDict(request.body.decode('utf-8')).dict()
            new_tanggal_lahir = data['tanggal_lahir']
            new_description = data['description']
            
            if new_tanggal_lahir is not None:
                user_profile.tanggal_lahir = new_tanggal_lahir
            if new_description is not None:
                user_profile.description = new_description

            # Save changes to the user profile
            user_profile.save()
            user_data = {
             "username" : user_profile.name,
             "role" : user_profile.role,
             "tanggalLahir" : user_profile.tanggal_lahir,
             "description" : user_profile.description,
            }
            
            return JsonResponse({"status": "success", "msg" : "data user berhasil diubah", "data" : user_data}, status=200)
    except User.DoesNotExist:
            return JsonResponse({"status" : "error", 'msg': 'user tidak ada silahkan login'}, status=401)
    except User.DoesNotExist:
        return JsonResponse({"status" : "error", 'msg': 'user profile tidak ada '}, status=404)
    except Exception as e:
            return JsonResponse({"status" : "error", 'msg': str(e)}, status=500)    
    
@csrf_exempt
@login_required(login_url='/auth/login')
def add_favorit_flutter(request, book_id):
    if request.method == 'POST':
        user = request.user
        try:
            buku = Buku.objects.get(pk=book_id)
            if not Favorit.objects.filter(user=user, id_book=buku.pk).exists():
                favorite = Favorit(user=user, id_book=buku.pk, title = buku.title, authors = buku.authors, language_code = buku.language_code,
                                   num_pages = buku.num_pages, publication_date = buku.publication_date,publisher = buku.publisher)
                favorite.save()
                return JsonResponse({'status' : 'success', 'msg': 'Add to Favorite successfully'}, status=200)
            else:
                return JsonResponse({'status' : 'failed', 'msg': 'Book is already favorited'}, status=400)
        except Buku.DoesNotExist:
            return JsonResponse({'status' : 'failed', 'msg': 'Book not found'}, status=400)
    return JsonResponse({'status' : 'failed', 'msg': 'Invalid request'}, status=400)

@login_required
def get_favorite_by_user_flutter(request):
    user = request.user

    print(user.username)
    favorites = Favorit.objects.filter(user = user).all()
    user_favorites = []
    for buku in favorites:
        user_favorites.append({
            'user_id' : buku.user.pk,
            'id_book' : buku.id_book,
            'authors' : buku.authors,
            'title' : buku.title,
            'language_code' : buku.language_code,
            'num_pages' : buku.num_pages,
            'publication_date' : buku.publication_date,
            'publisher' : buku.publisher,
        })
    return JsonResponse({'status' : 'success','data' : user_favorites} , content_type="application/json")

@csrf_exempt
@login_required(login_url='/auth/login')
def delete_favorite_flutter(request, book_id):
    if request.method == 'POST':
        user = request.user
        try:
            buku = Buku.objects.get(pk=book_id)
            favorite = Favorit.objects.filter(user=user, id_book=buku.pk).first()
            if favorite:
                favorite.delete()
                return JsonResponse({'status' : 'success','msg': 'Removed from Favorite successfully'}, status=200)
            else:
                return JsonResponse({'status' : 'failed', 'msg': 'Book is not favorited'}, status=400)
        except Buku.DoesNotExist:
            return JsonResponse({'status' : 'failed', 'msg': 'Book not found'}, status=400)
    return JsonResponse({'status' : 'failed', 'msg': 'Invalid request'}, status=400)