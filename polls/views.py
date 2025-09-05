from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice
from django.template import loader
from django.shortcuts import render
from django.http import Http404

# Create your views here.
def index (request):
    latest_question_list = Question.objects.all()
    template_name = "polls/index.html"
    # template = loader.get_template(template_name)
    context = {'latest_question': latest_question_list}
    return render(request,template_name,context)

    # return HttpResponse(template.render(context, request))
    # return HttpResponse("," .join([question.question_text for question in latest_question_list]))
def detail(request, question_id):
    question = get_object_or_404(Question,id=question_id)
    # try:
    #     question = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
        # return HttpResponse("Question doesn't exist")

    return render(request, "polls/detail.html" ,{'question':question})

    # return HttpResponse("Question doesn't exist")
    # return HttpResponse(f"You're looking at question {question_id}")

def vote(request, question_id):
    question = get_object_or_404(Question,id=question_id)
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {'question': question, 'error_message': "You didn't select a choice."}
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
def results(request, question_id):
    return HttpResponse(f"You're looking at result {question_id}")

