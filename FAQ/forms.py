from django.forms import ModelForm
from FAQ.models import Question, QuestionAnswer

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["isi_pertanyaan"]

class QuestionAnswerForm(ModelForm):
    class Meta:
        model = QuestionAnswer
        fields = ["isi_pertanyaan","isi_jawaban"]