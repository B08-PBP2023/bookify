from django.urls import path
from FAQ.views import delete_question_answer_flutter, delete_question_flutter, jawab_question_flutter, show_page, add_question, view_list_questions, get_questions_json, delete_question, jawab_question, get_questions_answers_json
from FAQ.views import delete_question_answer, show_page_admin, show_buku, get_questions_answers_filtered_json, get_questions_filtered_json, get_questions_by_id_json
from FAQ.views import get_books, add_question_flutter

app_name = 'FAQ'

urlpatterns = [
    path('', show_buku, name = 'show_buku'),
    path('show_page/<int:id_book>/', show_page, name = 'show_page'),
    #path('show_page_admin/<int:id_book>/', show_page_admin, name = 'show_page_admin'),
    path('add_question/<int:id_book>/', add_question, name = 'add_question'),
    path('view_list_questions/<int:id_book>/', view_list_questions, name = 'view_list_questions'),
    path('delete_question/<int:id>/', delete_question, name='delete_question'),
    path('delete_question_flutter/<int:id>/', delete_question_flutter, name='delete_question_flutter'),

    path('delete_question_answer/<int:id>/', delete_question_answer, name='delete_question_answer'),
    path('delete_question_answer_flutter/<int:id>/', delete_question_answer_flutter, name='delete_question_answer_flutter'),

    path('jawab_question/<int:id_book>/', jawab_question, name='jawab_question'),

    path('get_books/', get_books, name='get_books'),
    path('get_questions_json/', get_questions_json, name='get_questions_json'),
    path('get_questions_filtered_json/<int:id>/', get_questions_filtered_json, name='get_questions_filtered_json'),
    path('get_questions_by_id_json/<int:id_question>/', get_questions_by_id_json, name='get_questions_by_id_json'),

    path('get_questions_answers_json/', get_questions_answers_json, name='get_questions_answers_json'),
    path('get_questions_answers_filtered_json/<int:id>/', get_questions_answers_filtered_json, name='get_questions_answers_filtered_json'),
    path('add_question_flutter/<int:id_book>/', add_question_flutter, name='add_question_flutter'),
    path('jawab_question_flutter/<int:id_book>/', jawab_question_flutter, name='jawab_question_flutter'),

    

]