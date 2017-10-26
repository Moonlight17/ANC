 # -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from flask import Flask, render_template, request, redirect
from django.urls import reverse
from django.template import loader, RequestContext
from django.views.generic import ListView, DetailView, CreateView
from .models import Spisok, TitleList, LaunchOperationTypes, EventTypes, PayloadClasses, DocSources


class IndexView(ListView):
	template_name = 'polls/main.html'
	context_object_name = 'context'
	
	def get_queryset(self):
		return Spisok.objects.order_by('id')


#DS
class DocSourcesOutput(ListView):
	template_name = 'polls/List/DS.html'
	context_object_name = 'context'


	def get_queryset(self):

		return DocSources.objects.order_by('id')


#TL
class TitleListOutput(ListView):
	template_name = 'polls/List/TL.html'
	context_object_name = 'context'


	def get_queryset(self):

		return TitleList.objects.order_by('id')	


#LOT
class LaunchOperationTypesOutput(ListView):
	template_name = 'polls/List/LOT.html'
	context_object_name = 'context'


	def get_queryset(self):

		return LaunchOperationTypes.objects.order_by('id')	


#ET
class EventTypesOutput(ListView):
	template_name = 'polls/List/ET.html'
	context_object_name = 'context'


	def get_queryset(self):

		return EventTypes.objects.order_by('id')	


#PC
class PayloadClassesOutput(ListView):
	template_name = 'polls/List/PC.html'
	context_object_name = 'context'


	def get_queryset(self):

		return PayloadClasses.objects.order_by('id')