import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from authentication.models import UserWithRole
from django.core import serializers
from pinjamBuku.models import Buku

# Create your views here.
list_of_admins = ['adminbookify']

@login_required(login_url='/authentication/login/')
def show_homepage(request):
    try:
        user_with_role = UserWithRole.objects.get(user=request.user)
    except:
        return HttpResponseRedirect(reverse('authentication:login'))
    role = user_with_role.role
    if(request.user.username in list_of_admins):
        role = 'Admin'
        
    context = {
        'name': request.user.username,
        'role': role,
    }

    return render(request, "homepage.html", context)

def show_homepage_guest(request):
    context = {

    }

    return render(request, "homepage_guest.html", context)

@login_required(login_url='/authentication/login/')
def show_list_of_books(request):
    context={

    }
    return render(request, "show_list_of_books.html", context)

def show_list_of_books_guest(request):
    context={

    }
    return render(request, "show_list_of_books_guest.html", context)

def get_books(request):
    books = Buku.objects.all()

    return HttpResponse(serializers.serialize('json', books))