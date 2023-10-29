from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Buku
from .forms import BookRequestForm
from django.views.decorators.csrf import csrf_exempt
from FAQ.models import Question, QuestionAnswer
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.core import serializers
# from pinjamBuku.models import Buku



def show_home(request):
    books = Buku.objects.all()
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
            form.instance.user = request.user  # Mengisi user dengan objek User saat menyimpan form.
            form.save()
            return redirect('requestBuku:show_home')
    else:
        form = BookRequestForm()
    return render(request, 'book_request.html', {'form': form})


# @login_required
# def book_request(request):
#     if request.method == 'POST':
#         form = BookRequestForm(request.user, request.POST)
#         if form.is_valid(): 
#             form.save()
#             return redirect('home')
#     else:
#         form = BookRequestForm()
#     return render(request, 'book_request.html', {'form': form})

def get_books(request):
    books = Buku.objects.all()
    return HttpResponse(serializers.serialize('json',books))

# def view_request(request):

#     books = Book.objects.all()
    
#     context = {
#         'books' : books,
#     }
#     return render (request, 'home.html', context)