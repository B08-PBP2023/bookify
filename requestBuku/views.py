from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import BukuReq
from .forms import BookRequestForm
from django.views.decorators.csrf import csrf_exempt
from FAQ.models import Question, QuestionAnswer
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.core import serializers


def show_home(request):
    books = BukuReq.objects.all()
    print(books)
    context = {
        'books' : books,
    }
    return render(request, "show_home.html", context)

@login_required
def book_request(request):
    if request.method == 'POST':
        form = BookRequestForm(request.POST)
        
        if form.is_valid():
            print("VALIDD")
            form.instance.user = request.user  
            form.save()
            return redirect('requestBuku:show_home')
    else:
        form = BookRequestForm()
    return render(request, 'book_request.html', {'form': form})


def get_books(request):
    books = BukuReq.objects.all()
    return HttpResponse(serializers.serialize('json',books))

def delete_request(request, id):
    product = BukuReq.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('requestBuku:show_home'))
