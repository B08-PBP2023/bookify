from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from FAQ.models import Question
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.core import serializers

# Create your views here.

def show_page(request):

    context = {
        
    }

    return render(request, 'faqpage.html', context)

@csrf_exempt
def add_question(request):
    if request.method == 'POST':
        isi_pertanyaan = request.POST.get("isi_pertanyaan")

        new_item = Question(isi_pertanyaan=isi_pertanyaan)
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

def view_list_questions(request):

    questions = Question.objects.all()

    context = {
        'questions' : questions, 
    }

    return render(request, 'listquestions.html', context)

def get_questions_json(request):
    questions = Question.objects.all()
    
    return HttpResponse(serializers.serialize('json', questions))





