from django.contrib import admin
from FAQ.models import Question, QuestionAnswer
# Register your models here.

admin.site.register(Question)
admin.site.register(QuestionAnswer)
