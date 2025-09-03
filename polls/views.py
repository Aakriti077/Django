from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
# Create your views here.
def index (request):
    latest_question_list = Question.objects.all()
    template_name = "polls/index.html"
    template = loader.get_template(template_name)
    context = {'latest_question_list': latest_question_list}
    return HttpResponse(template.render(context, request))
    # return HttpResponse("," .join([question.question_text for question in latest_question_list]))

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")

def result(request, question_id):
    return HttpResponse(f"You're looking at result {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You're looking at vote {question_id}")