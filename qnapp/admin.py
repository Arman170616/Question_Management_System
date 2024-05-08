from django.contrib import admin
from .models import AllQuestions

@admin.register(AllQuestions)
class AllQuestionsAdmin(admin.ModelAdmin):
    list_display = ('Question_Title', 'Answer')
    search_fields = ['Question_Title']
