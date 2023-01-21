from .models import QuestionTypes,Questions,Questionnaire
from django import forms
from demarcate.models import demarcateQuestion
class QuestionTypeForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=QuestionTypes.objects.all(), to_field_name="category", empty_label="Select Category")
    class Meta:
        model = QuestionTypes
        fields = '__all__'

class CreateQuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'
        exclude = ['typequestionandidtypequestion']
        

class CreateQuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = '__all__'


class createImageQuestion(forms.ModelForm):
    class Meta:
        model = demarcateQuestion 
        fields = '__all__'
        exclude = ('x','y','w','h','area')