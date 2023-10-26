from django.urls import path
from FAQ.views import show_page, add_question, view_list_questions, get_questions_json, delete_question

app_name = 'FAQ'

urlpatterns = [
    path('', show_page, name = 'show_page'),
    path('add_question/', add_question, name = 'add_question'),
    path('view_list_questions/', view_list_questions, name = 'view_list_questions'),
    path('get_questions_json/', get_questions_json, name='get_questions_json'),
    path('delete_question/<int:id>/', delete_question, name='delete_question'),

]