from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    prof_pict = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)  # Ganti dengan field yang sesuai dengan penilaian Anda
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username}'

    class Meta:
        ordering = ['-created_at']


# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.

# class Review(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     ulasan = models.TextField(null=True, blank=True)
#     date_added = models.DateField(auto_now_add=True)
#     rating = models.IntegerField()