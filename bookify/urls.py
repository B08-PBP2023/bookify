"""
URL configuration for bookify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Homepage.urls')),
    path('authentication/', include('authentication.urls')),
    path('pinjamBuku/',include('pinjamBuku.urls')),
    path('profilUser/', include ('profilUser.urls')),
    path('FAQ/',include('FAQ.urls')),
    path('requestBuku/',include('requestBuku.urls')),
    path('ulasanBuku/',include('ulasanBuku.urls')),
    path('BacaDanWishlist/', include('BacaDanWishlist.urls')),
    path('auth/', include('flutter_authentication.urls')),
]