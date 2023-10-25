from django.shortcuts import render

# Create your views here.

def show_page(request):

    context = {
        
    }

    return render(request, 'faqpage.html', context)
