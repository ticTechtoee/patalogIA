from django.shortcuts import render

def covid(request):
    return render(request, 'predication/covid/index.html')


def tuberculose(request):
    return render(request, 'predication/tuberculose/index.html')
