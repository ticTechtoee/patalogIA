from django.urls import path, include
from . import views

app_name = 'questions'


urlpatterns = [
    path('',views.question, name='questiontype'),
    path('demarcate',views.createDemarcate, name='demarcatePage'),
    path('MCQs',views.MCQs, name='MCQsPage'),
    path('quiz',views.showQuestions, name='quiz'),
    path('quizdetail/<str:pk>', views.quizdetail, name='quizdetail'),
    path('demarcateQuiz', views.demarcateQuiz, name='demarcateQuiz'),
    path('demarcateQuizDetail/<str:pk>', views.demarcateQuizDetail, name = 'demarcateQuizDetail')

]
