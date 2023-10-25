import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse, HttpResponse
from django.urls import reverse
from django.core import serializers

# Create your views here.
@login_required(login_url='/authentication/login/')
def show_homepage(request):
    context = {
        'name': request.user.username,
        'class': 'PBP B',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "homepage.html", context)