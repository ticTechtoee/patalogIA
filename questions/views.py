from django.shortcuts import render, redirect
from .forms import QuestionTypeForm,CreateQuestionsForm,CreateQuestionnaireForm, uploadImageForm
from .models import Questions, Questionnaire, AlternativeQuestions
from demarcate.models import demarcate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import math

def question(request):
    form = QuestionTypeForm(request.POST or None)
    if form.is_valid():
        if str(form.cleaned_data.get('category')) == 'Demarcate':
            return redirect('questions:demarcatePage')
        elif str(form.cleaned_data.get('category')) == 'Multiple Choice Questions':
            return redirect('questions:MCQsPage')
    context = {'form':form}
    return render(request, 'questions/teacher/questionType.html', context)\

"""-------------------------------------------------------------------------------------------------------"""
"""Demarcate Question and Answer Section"""
@csrf_exempt
def createDemarcate(request):
    """Process images uploaded by users"""
    form = uploadImageForm(request.POST or None)
    if request.method == "POST":
        form = uploadImageForm(request.POST,request.FILES)
        instance = form.save(commit=False)
        x1 = int(request.POST.get("x1"))
        y1 = int(request.POST.get("y1"))
        x2 = int(request.POST.get("x2"))
        y2 = int(request.POST.get("y2"))
        getArea = findarea(x1,x2,y1,y2)
        createPoints  = demarcate(x = x1, y = y1, w = (x2 - x1), h = (y2 - y1), area = getArea, idimage = instance)
        instance.save()
        createPoints.save()
    return render(request, 'questions/teacher/demarcatePage.html', {'form':form})

def findarea(x1,x2,y1,y2):
    wSqrOfX =  (x2-x1) ** 2
    wSqrOfY = (y2-y1) ** 2
    sumOfSquares = wSqrOfX + wSqrOfY
    area = math.sqrt(sumOfSquares)
    return area


# def demarcate(request):

#     return render(request,'questions/student/demarcatePage.html')

"""-------------------------------------------------------------------------------------------------------"""

def MCQs(request):
    form = CreateQuestionsForm(request.POST or None)
    if form.is_valid():
        print('MCQ Created')
        form.save()
    context = {'form':form}
    return render(request, 'questions/teacher/MCQsPage.html', context)

def showQuestions(request):
    descQuesiton = Questions.objects.all()
    context = {'QuestionText':descQuesiton}
    return render(request, 'questions/student/quiz.html', context)

def quizdetail(request, pk):
    getOptions = AlternativeQuestions.objects.filter(questoes_questoes_id__description = pk)
    rightAns = Questions.objects.get(description = pk)
    getQuestion = pk
    context = {'Question':getQuestion,'Options': getOptions}

    if request.method == "POST":
        selectedOptionA = request.POST.get('A')
        selectedOptionB = request.POST.get('B')
        selectedOptionC = request.POST.get('C')
        selectedOptionD = request.POST.get('D')

        if selectedOptionA == rightAns.certain:
            print('A Your Answer is correct')
            return HttpResponse('Your Answer is Correct')
        elif selectedOptionB == rightAns.certain:
            print('B Your Answer is correct')
            return HttpResponse('Your Answer is Correct')
        elif selectedOptionC == rightAns.certain:
            print('C Your Answer is correct')
            return HttpResponse('Your Answer is Correct')
        elif selectedOptionD == rightAns.certain:
            print('D Your Answer is correct')
            return HttpResponse('Your Answer is Correct')

    return render(request, 'questions/student/questionwithoptions.html', context)