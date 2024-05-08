from django.shortcuts import render
from .models import AllQuestions


def question_list_view(request):
    questions = AllQuestions.objects.all()
    return render(request, 'question_list.html', {'questions': questions})

def question_detail_view(request, question_id):
    question = AllQuestions.objects.get(pk=question_id)
    return render(request, 'question_detail.html', {'question': question})
