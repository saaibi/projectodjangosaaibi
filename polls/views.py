from django.http import HttpResponse
from .models import Question
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
	return HttpResponse("Usted se encuentra en la pregunta %s." % question_id)


def results(request, question_id):
	response = "Se encuenra en los resultado de la pregunta %s. "
	return HttpResponse(response % question_id)


def vote(request, question_id):
	return HttpResponse("Usted esta votando en la pregunta %s." % question_id)