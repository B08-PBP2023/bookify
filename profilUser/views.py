from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

def show_page(request):

    context = {
        
    }

    return render(request, 'profil.html', context)

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'userprofile/profil.html', {'user_profile': user_profile})

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = UserProfileForm()
    return render(request, 'userprofile/create_profil.html', {'form': form})

@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'userprofile/edit_profil.html', {'form': form})
