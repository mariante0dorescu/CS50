from .models import Question, Choice
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.utils import timezone

# Create your views here.

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, "polls/detail.html", {"question":question})


def vote(request, question_id):
  question = get_object_or_404(Question, pk = question_id)
  try:
    selected_choice = question.choice_set.get(pk = request.POST['choice'])
  except(KeyError, Choice.DoesNotExist):
    return render(request, "polls/detail.html", {
      "question":question,
      "error_message":"You didn't select a choice",
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))


def results(request, question_id):
  question = get_object_or_404(Question, pk = question_id)
  choices = question.choice_set.all().order_by('-votes')
  return render(request, "polls/results.html", {"question":question, 'choices': choices})
  #return HttpResponse('You are looking at the results of question %s' % question_id)


class IndexView(generic.ListView):
  template_name = "polls/index.html"
  context_object_name = 'latest_questions_list'

  def get_queryset(self):
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
  

class DetailView(generic.DetailView):
  model = Question
  template_name = "polls/detail.html"

  def get_queryset(self):
    return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = context['object']  # The current Question object

        # Get the choices for the current question and sort them by votes
        choices = Choice.objects.filter(question=question).order_by('-votes')

        # Add the question and sorted choices to the context
        context['question'] = question
        context['choices'] = choices

        return 
        
# def index(request):
#   latest_questions_list = Question.objects.order_by("-pub_date")[:5]
#   #output = ", ".join([q.question_text for q in latest_questions_list])
#   template = loader.get_template("polls/index.html")
#   context = {"latest_questions_list" : latest_questions_list}
#   return HttpResponse(template.render(context, request))
#   #return HttpResponse('hello')
  # try:
  #   question = Question.objects.get(pk=question_id)
  # except:
  #   # return HttpResponseNotFound('question does not exists.')
  #   raise Http404('question does not exists.')
  # return HttpResponse('You are looking at question %s.' % question_id)
  # question = get_object_or_404(Question, pk=question_id)
  # return HttpResponse(question)
  # return render(request, "polls/detail.html", {
  #   "question" : question,
  # })
  # try:
  #   question = Question.objects.get(pk=question_id)
  # except question.DoesNotExists:
  #   #raise Http404('question does not exists.')
  #   return HttpResponseNotFound('question does not exists.')
  # return HttpResponse('You are looking at question %s.' % question_id)

# def vote(request, question_id):
#   return HttpResponse('You are voting on question %s' % question_id)

# class DetailView(generic.DetailView):
#   model = Question
#   template_name = "polls/detail.html"

# class ResultsView(generic.DetailView):
#   model = Question
#   template_name = "polls/results.html"