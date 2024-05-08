from django.shortcuts import render
from .models import AllQuestions


def question_list_view(request):
    questions = AllQuestions.objects.all()
    return render(request, 'question_list.html', {'questions': questions})

def question_detail_view(request, question_id):
    question = AllQuestions.objects.get(pk=question_id)
    return render(request, 'question_detail.html', {'question': question})


# def question_list_view(request):
#     # Retrieve all categories from your database or any source
#     # For example, assuming 'Category' is a field in your AllQuestions model
#     categories = AllQuestions.objects.values_list('Category', flat=True).distinct()

#     # Check if a category filter is applied
#     category_filter = request.GET.get('category')

#     # Filter questions based on the selected category
#     if category_filter:
#         questions = AllQuestions.objects.filter(Category=category_filter)
#     else:
#         questions = AllQuestions.objects.all()

#     return render(request, 'question_list.html', {'questions': questions, 'categories': categories})