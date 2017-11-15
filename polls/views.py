 # -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from flask import Flask, render_template, request, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.template import loader, RequestContext
from django.views.generic import ListView, DetailView, CreateView, View, FormView
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


class RegisterView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/polls/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration_form.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterView, self).form_valid(form)






# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.


class LoginView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "registration_form.html"

    # В случае успеха перенаправим на главную.
    success_url = "/polls/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)

        return super(LoginView, self).form_valid(form)






class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/polls/")






























