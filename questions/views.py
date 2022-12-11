from django.shortcuts import render, redirect
from .forms import QuestionTypeForm,CreateQuestions,CreateQuestionnaire
from .models import Questions, Questionnaire, AlternativeQuestions
from django.http import HttpResponse

def question(request):
    form = QuestionTypeForm(request.POST or None)
    if form.is_valid():
        if str(form.cleaned_data.get('category')) == 'Demarcate':
            return redirect('questions:demarcatePage')
        elif str(form.cleaned_data.get('category')) == 'Multiple Choice Questions':
            return redirect('questions:MCQsPage')
    context = {'form':form}
    return render(request, 'questions/teacher/questionType.html', context)

def demarcate(request):
    form = CreateQuestions(request.POST or None)
    if form.is_valid():
        print('Demarcate Created')
    context = {'form':form}
    return render(request, 'questions/teacher/demarcatePage.html', context)


def MCQs(request):
    form = CreateQuestions(request.POST or None)
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