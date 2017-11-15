
 # -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from flask import Flask, render_template, request, redirect
from django.core.urlresolvers import reverse_lazy
from django.urls import reverse
from django.template import loader, RequestContext
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import EventTypes


class DetailView(DetailView):
    model = EventTypes
    template_name = 'polls/ET/Detail.html'

class EventTypesCreate(CreateView):
	model = EventTypes
	fields = ['title','ready','doc_note','doc_text','date']

class EventTypesUpdate(UpdateView):
	model = EventTypes
	fields = ['title','ready','doc_note','doc_text']

class EventTypesDelete(DeleteView):
	model = EventTypes
	success_url = reverse_lazy('polls:ET')








