import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse, HttpResponse
from django.urls import reverse
from django.core import serializers
from pinjamBuku.models import Buku

# Create your views here.
@login_required(login_url='/authentication/login/')
def show_homepage(request):
    context = {
        'name': request.user.username,
    }

    return render(request, "homepage.html", context)

def show_homepage_guest(request):
    context = {

    }

    return render(request, "homepage_guest.html", context)

def show_list_of_books(request):
    context={

    }
    return render(request, "show_list_of_books.html", context)

def get_books(request):
    books = Buku.objects.all()

    return HttpResponse(serializers.serialize('json', books))