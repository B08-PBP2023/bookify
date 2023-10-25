# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render, redirect
# from .models import UserProfile
# from .forms import UserProfileForm  # Anda perlu membuat form untuk mengedit profil

# def view_profile(request):
#     # Dapatkan profil pengguna yang sesuai dengan pengguna yang saat ini masuk
#     user_profile = UserProfile.objects.get(user=request.user)

#     return render(request, 'profil.html', {'user_profile': user_profile})

# def edit_profile(request):
#     # Dapatkan profil pengguna yang sesuai dengan pengguna yang saat ini masuk
#     user_profile = UserProfile.objects.get(user=request.user)

#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             return redirect('view_profile')

#     else:
#         form = UserProfileForm(instance=user_profile)

#     return render(request, 'edit_profile.html', {'form': form})

