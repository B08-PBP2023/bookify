import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from FAQ.models import Question, QuestionAnswer
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from authentication.models import UserWithRole
from pinjamBuku.models import Buku
from FAQ.forms import QuestionForm, QuestionAnswerForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Homepage.views import list_of_admins
# Create your views here.

@login_required(login_url='/authentication/login/')
def show_buku(request):

    books = Buku.objects.all()

    if(request.user.username in list_of_admins):

        context = {
            'books':books,
            'name':request.user.username,
            'role':'Admin',
        }
        return render(request, 'show_buku_admin.html', context)
    
    try:
        user_with_role = UserWithRole.objects.get(user=request.user)
    except:
        return HttpResponseRedirect(reverse('authentication:login'))
    
    context = {
        'books':books,
        'name':request.user.username,
        'role':user_with_role.role,
    }

    return render(request, 'show_buku.html', context)

@login_required(login_url='/authentication/login/')
def show_page(request, id_book):
    context = {
        'id_book' : id_book,
    }
    if(request.user.username in list_of_admins):
        return render(request, 'faqpage_admin.html', context)
    
    form = QuestionForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)

        item.save()
        return render(request, 'faqpage.html', context)
    
    context = {
        'id_book' : id_book,
        'form':form,
    }

    return render(request, 'faqpage.html', context)

@login_required(login_url='/authentication/login/')
def show_page_admin(request,id_book):
    context = {
        'id_book' : id_book,
    }
    return render(request, 'faqpage_admin.html', context)

@login_required(login_url='/authentication/login/')
def view_list_questions(request, id_book):

    if(request.user.username not in list_of_admins):
        return HttpResponseNotFound()
    
    context = {
        'id_book' : id_book,
    }
    form = QuestionAnswerForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)

        item.save()
        return render(request, 'listquestions.html', context)
    
    context = {
        'id_book' : id_book,
        'form':form,
    }

    return render(request, 'listquestions.html', context)




@csrf_exempt
@login_required(login_url='/authentication/login/')
def jawab_question(request, id_book):
    if request.method == 'POST':
        buku = Buku.objects.get(pk=id_book)
        judul_buku = buku.title
        isi_pertanyaan = request.POST.get("isi_pertanyaan")
        isi_jawaban = request.POST.get("isi_jawaban")


        new_item = QuestionAnswer(isi_pertanyaan=isi_pertanyaan, isi_jawaban=isi_jawaban, buku = buku)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def jawab_question_flutter(request, id_book):
    if request.method == 'POST':
        buku = Buku.objects.get(pk=id_book)
        data = json.loads(request.body)

        isi_pertanyaan = data["isi_pertanyaan"]
        isi_jawaban = data["isi_jawaban"]
        idQuestion = int(data["id_question"])

        question = Question.objects.get(pk=idQuestion)
        question.delete()

        new_item = QuestionAnswer(isi_pertanyaan=isi_pertanyaan, isi_jawaban=isi_jawaban, buku = buku)
        new_item.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
@login_required(login_url='/authentication/login/')
def add_question(request, id_book):
    if request.method == 'POST':
        buku = Buku.objects.get(pk=id_book)

        judul_buku = buku.title
        isi_pertanyaan = request.POST.get("isi_pertanyaan")

        new_item = Question(isi_pertanyaan=isi_pertanyaan, buku=buku)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def add_question_flutter(request, id_book):
    if request.method == 'POST':
        buku = Buku.objects.get(pk=id_book)
        data = json.loads(request.body)
        isi_pertanyaan = data["isi_pertanyaan"]

        new_item = Question(isi_pertanyaan=isi_pertanyaan, buku=buku)
        new_item.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
@login_required(login_url='/authentication/login/')
def delete_question(request,id):
    if request.method == 'DELETE':
        data = Question.objects.get(pk=id)
        data.delete()

        return HttpResponse(b"DELETE", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_question_flutter(request,id):
    if request.method == 'POST':
        data = Question.objects.get(pk=id)
        data.delete()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def delete_question_answer_flutter(request,id):
    if request.method == 'POST':
        data = QuestionAnswer.objects.get(pk=id)
        data.delete()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
@login_required(login_url='/authentication/login/')
def delete_question_answer(request,id):
    if request.method == 'DELETE':
        data = QuestionAnswer.objects.get(pk=id)
        data.delete()

        return HttpResponse(b"DELETE", status=201)

    return HttpResponseNotFound() 


def get_questions_json(request):
    questions = Question.objects.all()
    
    return HttpResponse(serializers.serialize('json', questions))

def get_questions_by_id_json(request, id_question):
    questions = Question.objects.filter(pk=id_question)
    
    return HttpResponse(serializers.serialize('json', questions))

def get_questions_answers_json(request):
    questions_answers = QuestionAnswer.objects.all()

    
    return HttpResponse(serializers.serialize('json', questions_answers))

def get_questions_answers_filtered_json(request, id):
    buku = Buku.objects.get(pk=id)
    judul_buku = buku.title

    questions_answers = QuestionAnswer.objects.filter(buku = buku)
    
    return HttpResponse(serializers.serialize('json', questions_answers))

def get_questions_filtered_json(request, id):
    buku = Buku.objects.get(pk=id)
    judul_buku = buku.title
    
    questions_answers = Question.objects.filter(buku = buku)
    
    return HttpResponse(serializers.serialize('json', questions_answers))

def get_books(request):
    books = Buku.objects.all()

    return HttpResponse(serializers.serialize('json', books))






