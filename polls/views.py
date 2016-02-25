from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola Mundo")


def detail(request, question_id):
	return HttpResponse("Usted se encuentra en la pregunta %s." % question_id)


def results(request, question_id):	
    response = "se encuentra en los resultados de la pregunta %s. "
    return HttpResponse(response % question_id)   


def vote(request, question_id):
    return HttpResponse("Usted esta votamdo en la pregunta %s." % question_id)    