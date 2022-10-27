from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse 
from .models import Question, Answer

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def paginate(request, qs):
    limit = 10
    page = request.GET.get('page', 1)
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page

@require_GET
def question(request, id = None):
    question = get_object_or_404(Question, id=id)
    answers = Answer.objects.filter(question=id)
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
    })

def new_questions(request):
    new_questions = Question.objects.new()
    questions = paginate(request, new_questions)
    return render(request, 'new.html', {
        'questions': questions,
    })

def popular(request):
    popular_questions = Question.objects.popular()
    questions = paginate(request, popular_questions)
    return render(request, 'popular.html', {
        'questions': questions,
    })
