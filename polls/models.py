from datetime import datetime
from django.urls import reverse
from django import forms
from django.db import models
from django.utils import timezone




class Spisok(models.Model):
	doc_ready = models.BooleanField(max_length=1500, verbose_name='Готовность')
	doc_title = models.CharField(max_length=200, default = "Title", verbose_name='Название')
	doc_note = models.CharField(max_length=400, blank=True, verbose_name='Подсказка' )
	date = models.DateTimeField(default=datetime.now, verbose_name='Дата')
	def __str__(self):
		return self.doc_title


#TL
class TitleList(models.Model):  
	title = models.CharField(max_length=200,  verbose_name='Название') 
	ready = models.BooleanField(max_length=1500, blank=True, verbose_name='Готовность')
	doc_specification = models.CharField(max_length=500, verbose_name='Спецификация')
	doc_note = models.CharField(max_length=400, verbose_name='Заметка' )
	doc_text = models.TextField(max_length=1500,  verbose_name='Текст')
	upload = models.ImageField(blank=True, upload_to='images/blog/%Y/%m/%d', help_text='150x150px', verbose_name='Изображение')
	date = models.DateTimeField(default=datetime.now)
	def __str__(self):
		return self.doc_note
	def get_absolute_url(self):
		return reverse('polls:TL')

	def data(self):
		return TitleList.objects.filter(id=self.id)

#LOT
class LaunchOperationTypes(models.Model):  
	title = models.CharField(max_length=200, default = "Title", verbose_name='Заголовок') 
	ready = models.BooleanField(max_length=1500, blank=True, verbose_name='Готовность')
	doc_specification = models.CharField(max_length=500, default = "Specification", verbose_name='Спецификация')
	doc_note = models.CharField(max_length=400, blank=True, verbose_name='Заметка' )
	doc_text = models.TextField(max_length=1500, default = "Text", verbose_name='Текст')
	date = models.DateTimeField(default=datetime.now, verbose_name='Дата')
	def __str__(self):
		return self.doc_note

	def get_absolute_url(self):
		return reverse('polls:LOT')

	def data(self):
		return LaunchOperationTypes.objects.filter(id=self.id)


#ET
class EventTypes(models.Model):  
	title = models.CharField(max_length=200, default = "Title", verbose_name='Заголовок') 
	ready = models.BooleanField(max_length=1500, blank=True, verbose_name='Готовность')
	doc_note = models.CharField(max_length=400, blank=True, verbose_name='Заметка' )
	doc_text = models.TextField(max_length=1500, default = "Text", verbose_name='Текст')
	date = models.DateTimeField(default=datetime.now, verbose_name='Дата')	
	def __str__(self):
		return self.doc_note

	def get_absolute_url(self):
		return reverse('polls:ET')

	def data(self):
		return EventTypes.objects.filter(id=self.id)


#PC
class PayloadClasses(models.Model):
	title = models.CharField(max_length=200, default = "Title", verbose_name='Заголовок') 
	ready = models.BooleanField(max_length=1500, blank=True, verbose_name='Готовность')
	doc_text = models.TextField(max_length=1500, default = "Text", verbose_name='Текст')
	date = models.DateTimeField(default=datetime.now, verbose_name='Дата')
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('polls:PC')

	def data(self):
		return PayloadClasses.objects.filter(id=self.id)


#DS
class DocSources(models.Model):  
	title = models.CharField(max_length=200, default = "Title", verbose_name='Заголовок') 
	ready = models.BooleanField(max_length=1500, blank=True, verbose_name='Готовность')
	doc_note = models.CharField(max_length=400, verbose_name='Заметка')
	doc_text = models.TextField(max_length=400,verbose_name='Текст')
	date = models.DateTimeField(default=datetime.now, verbose_name='Дата')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('polls:DS')

	def data(self):
		return DocSources.objects.filter(id=self.id)










