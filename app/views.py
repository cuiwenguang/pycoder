from django.shortcuts import render


def index(request):
    return render(request,'app/index.html')

def course(request, c_name=None):
    return render(request, 'app/courselist.html')

def question_and_answer(request):
    return render(request, 'app/qa.html')

