
 # -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from flask import Flask, render_template, request, redirect
from django.core.urlresolvers import reverse_lazy
from django.urls import reverse
from django.template import loader, RequestContext
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import LaunchOperationTypes


class DetailView(DetailView):
    model = LaunchOperationTypes
    template_name = 'polls/LOT/Detail.html'

class LaunchOperationTypesCreate(CreateView):
	model = LaunchOperationTypes
	fields = ['title','ready','doc_note','doc_text','date']

class LaunchOperationTypesUpdate(UpdateView):
	model = LaunchOperationTypes
	fields = ['title','ready','doc_note','doc_text']

class LaunchOperationTypesDelete(DeleteView):
	model = LaunchOperationTypes
	success_url = reverse_lazy('polls:LOT')








