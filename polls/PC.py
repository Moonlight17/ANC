
 # -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from flask import Flask, render_template, request, redirect
from django.core.urlresolvers import reverse_lazy
from django.urls import reverse
from django.template import loader, RequestContext
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import PayloadClasses


class DetailView(DetailView):
    model = PayloadClasses
    template_name = 'polls/PC/Detail.html'

class PayloadClassesCreate(CreateView):
	model = PayloadClasses
	fields = ['title','ready','doc_text','date']

class PayloadClassesUpdate(UpdateView):
	model = PayloadClasses
	fields = ['title','ready','doc_note','doc_text']

class PayloadClassesDelete(DeleteView):
	model = PayloadClasses
	success_url = reverse_lazy('polls:PC')








