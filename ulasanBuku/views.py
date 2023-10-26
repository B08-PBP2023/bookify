from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from models import Review
from .forms import ReviewForm  # Anda perlu membuat form terlebih dahulu

@login_required
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_list')  # Ganti 'review_list' dengan nama URL yang sesuai
    else:
        form = ReviewForm()

    return render(request, 'create_review.html', {'form': form})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})

# Anda dapat menambahkan fungsi lain sesuai kebutuhan aplikasi Anda
