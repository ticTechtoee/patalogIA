from django.contrib import admin
from .models import Questions,AlternativeQuestions,QuestionTypes,Questionnaire,Result,Cases

admin.site.register(Questions)
admin.site.register(AlternativeQuestions)
admin.site.register(QuestionTypes)
admin.site.register(Questionnaire)
admin.site.register(Result)
admin.site.register(Cases)