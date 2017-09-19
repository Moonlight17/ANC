 # -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader, RequestContext
from django.views import generic
from .models import Spisok
from .forms import SpisokForm

class IndexView(generic.ListView):
    template_name = 'polls/main.html'
    context_object_name = 'latest_spisok_list'


    def get_queryset(self):
        """Return the last five published questions."""
        return Spisok.objects.order_by('id')




class DetailView(generic.DetailView):
    model = Spisok
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Spisok
    template_name = 'polls/results.html'




def vote():

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def text_new(request):
    text_form = SpisokForm(request.POST or None)
    if request.method == "POST":
            if text_form.is_valid():
                data = text_form.cleaned_data
                spisok = Spisok.objects.create(doc_ready=data['doc_ready'], doc_TXT=data['doc_TXT'])
                spisok.doc_ready = data['doc_ready']
                spisok.doc_TXT = data['doc_TXT']
                spisok.doc_title = data['doc_title']
                spisok.doc_specification = data['doc_specification']
                spisok.doc_note = data['doc_note']
                spisok.doc_text = data['doc_text']
                spisok.save()
    # return render(request, 'index.html')
    return HttpResponseRedirect(reverse('polls:index'))



def text_edit(request, spisok_id):
    spisok = get_object_or_404(Spisok, pk=spisok_id)
    text_form = SpisokForm(request.POST, instance=spisok)
    if request.method == "POST":
            if text_form.is_valid():
                data = text_form.cleaned_data
                spisok.doc_ready = data['doc_ready']
                spisok.doc_TXT = data['doc_TXT']
                spisok.doc_ready = data['doc_ready']
                spisok.doc_TXT = data['doc_TXT']
                spisok.doc_title = data['doc_title']
                spisok.doc_specification = data['doc_specification']
                spisok.doc_note = data['doc_note']
                spisok.doc_text = data['doc_text']
                spisok.save()
    # return render(request, 'index.html')
    return HttpResponseRedirect(reverse('polls:index'))

def text_delete(request, spisok_id):
    spisok = get_object_or_404(Spisok, pk=spisok_id)
    spisok.delete()
    return HttpResponseRedirect(reverse('polls:index'))





# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))