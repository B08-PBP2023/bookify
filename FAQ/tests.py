from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Buku, Question, QuestionAnswer
from authentication.models import UserWithRole
from .forms import QuestionForm, QuestionAnswerForm

class YourAppTests(TestCase):
    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user_with_role = UserWithRole.objects.create(user=self.user, name='testuser', role='Reguler')
        self.admin = User.objects.create_user(username='adminreal', password='testpassword')

        # Create some test data
        self.book = Buku.objects.create(title='Test Book')
        self.question = Question.objects.create(buku=self.book, isi_pertanyaan='Test Question')
        self.question_answer = QuestionAnswer.objects.create(buku=self.book, isi_pertanyaan='Test Question', isi_jawaban='Test Answer')

    # show_buku (Hanya bisa diakses user biasa dan admin)
    def test_show_buku_admin(self):
        self.client.login(username='adminreal', password='testpassword')
        response = self.client.get(reverse('FAQ:show_buku'))
        self.assertEqual(response.status_code, 200) # Jika admin, maka sukses

    def test_show_buku_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('FAQ:show_buku'))
        self.assertEqual(response.status_code, 200) # Jika user biasa, maka sukses

    def test_show_buku_guest(self):
        response = self.client.get(reverse('FAQ:show_buku'))
        self.assertEqual(response.status_code, 302)  # Ke page login karena Guest


    # show_page (Hanya bisa diakses user biasa dan admin)
    def test_show_page_guest(self):
        response = self.client.get(reverse('FAQ:show_page', args=[self.book.id]))
        self.assertEqual(response.status_code, 302) # Ke page login karena Guest

    def test_show_page_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('FAQ:show_page', args=[self.book.id]))
        self.assertEqual(response.status_code, 200) # Jika user biasa, maka sukses

    def test_show_page_admin(self):
        self.client.login(username='adminreal', password='testpassword')
        response = self.client.get(reverse('FAQ:show_page', args=[self.book.id]))
        self.assertEqual(response.status_code, 200) # Jika admin, maka sukses


    # view_list_questions (Hanya bisa diakses admin)
    def test_view_list_questions_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('FAQ:view_list_questions', args=[self.book.id]))
        self.assertEqual(response.status_code, 404) # Jika user biasa mencoba mengakses page admin, maka tidak bisa

    def test_view_list_questions_admin(self):
        self.client.login(username='adminreal', password='testpassword')
        response = self.client.get(reverse('FAQ:view_list_questions', args=[self.book.id]))
        self.assertEqual(response.status_code, 200) # Jika user biasa mencoba mengakses page admin, maka tidak bisa
    

    # get data json
    def test_get_questions_json(self):
        response = self.client.get(reverse('FAQ:get_questions_json'))
        self.assertEqual(response.status_code, 200)

    def test_get_questions_answers_json(self):
        response = self.client.get(reverse('FAQ:get_questions_answers_json'))
        self.assertEqual(response.status_code, 200)

    def test_get_books(self):
        response = self.client.get(reverse('FAQ:get_books'))
        self.assertEqual(response.status_code, 200)

    def test_get_questions_by_id_json(self):
        response = self.client.get(reverse('FAQ:get_questions_by_id_json', args=[self.question.id]))
        self.assertEqual(response.status_code, 200)

    def test_get_questions_answers_filtered_json(self):
        response = self.client.get(reverse('FAQ:get_questions_answers_filtered_json', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)

    def test_get_questions_filtered_json(self):
        response = self.client.get(reverse('FAQ:get_questions_filtered_json', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)

