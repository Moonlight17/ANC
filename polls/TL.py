
 # -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from flask import Flask, render_template, request, redirect
from django.core.urlresolvers import reverse_lazy
from django.urls import reverse
from django.template import loader, RequestContext
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TitleList


class DetailView(DetailView):
    model = TitleList
    template_name = 'polls/TL/TLDetail.html'

class TitleListCreate(CreateView):
	model = TitleList
	fields = ['title','ready','doc_specification','doc_note','doc_text', 'upload' ,'date']

class TitleListUpdate(UpdateView):
	model = TitleList
	fields = ['title','ready','doc_specification','doc_note','doc_text', 'upload']

class TitleListDelete(DeleteView):
	model = TitleList
	success_url = reverse_lazy('polls:TL')

