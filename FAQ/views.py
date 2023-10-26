from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from FAQ.models import Question, QuestionAnswer
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.core import serializers
from pinjamBuku.models import Buku

# Create your views here.

def show_buku(request):
    books = Buku.objects.all()

    context = {
        'books':books,
    }

    return render(request, 'show_buku.html', context)

def show_page(request, id_book):
    context = {
        'id_book' : id_book,
    }
    return render(request, 'faqpage.html', context)

def show_page_admin(request,id_book):
    context = {
        'id_book' : id_book,
    }
    return render(request, 'faqpage_admin.html', context)

@csrf_exempt
def add_question(request, id_book):
    if request.method == 'POST':
        buku = Buku.objects.get(pk=id_book)
        
        judul_buku = buku.title
        isi_pertanyaan = request.POST.get("isi_pertanyaan")

        new_item = Question(isi_pertanyaan=isi_pertanyaan, judul_buku=judul_buku)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_question(request,id):
    if request.method == 'DELETE':
        data = Question.objects.get(pk=id)
        data.delete()

        return HttpResponse(b"DELETE", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_question_answer(request,id):
    if request.method == 'DELETE':
        data = QuestionAnswer.objects.get(pk=id)
        data.delete()

        return HttpResponse(b"DELETE", status=201)

    return HttpResponseNotFound() 

def view_list_questions(request, id_book):

    # questions = Question.objects.all()

    context = {
        # 'questions' : questions, 
        'id_book' : id_book,
    }

    return render(request, 'listquestions.html', context)

def get_questions_json(request):
    questions = Question.objects.all()
    
    return HttpResponse(serializers.serialize('json', questions))

def get_questions_answers_json(request):
    questions_answers = QuestionAnswer.objects.all()
    print(questions_answers)
    
    return HttpResponse(serializers.serialize('json', questions_answers))

def get_questions_answers_filtered_json(request, id):
    buku = Buku.objects.get(pk=id)
    print(buku.title)
    print(QuestionAnswer.objects.all())
    questions_answers = QuestionAnswer.objects.filter(judul_buku = buku.title)
    print(questions_answers)
    
    return HttpResponse(serializers.serialize('json', questions_answers))

@csrf_exempt
def jawab_question(request, id_book):
    if request.method == 'POST':
        buku = Buku.objects.get(pk=id_book)
        judul_buku = buku.title
        isi_pertanyaan = request.POST.get("isi_pertanyaan")
        isi_jawaban = request.POST.get("isi_jawaban")


        new_item = QuestionAnswer(isi_pertanyaan=isi_pertanyaan, isi_jawaban=isi_jawaban, judul_buku=judul_buku)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()





