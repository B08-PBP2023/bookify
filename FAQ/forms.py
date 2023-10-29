from django.forms import ModelForm
from FAQ.models import Question, QuestionAnswer

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["isi_pertanyaan"]
    
    def __init__(self, args, **kwargs): 
        super().__init__(args, **kwargs) 
        self.fields['isi_pertanyaan'].widget.attrs.update({ 
            'required':'False', 
            'id':'isi_pertanyaan', 
            'class':"form-control"
        })
        self.fields['isi_pertanyaan'].label_attr = {'class': 'col-form-label'}

class QuestionAnswerForm(ModelForm):
    class Meta:
        model = QuestionAnswer
        fields = ["isi_pertanyaan","isi_jawaban"]

    def __init__(self, args, **kwargs): 
        super().__init__(args, **kwargs) 
        self.fields['isi_pertanyaan'].widget.attrs.update({ 
            'required':'False', 
            'id':'isi_pertanyaan', 
            'class':"form-control"
            
        })
        self.fields['isi_pertanyaan'].label_attr = {'class': 'col-form-label'}

        self.fields['isi_jawaban'].widget.attrs.update({ 
            'required':'False', 
            'id':'isi_jawaban', 
            'class':'form-control',
            
        })
        self.fields['isi_jawaban'].label_attr = {'class': 'col-form-label'}