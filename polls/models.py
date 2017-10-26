from datetime import datetime
from django.urls import reverse
from django import forms
from django.db import models
from django.utils import timezone




class Spisok(models.Model):
	doc_ready = models.BooleanField(max_length=1500)
	doc_title = models.CharField(max_length=200, default = "Title")
	doc_note = models.CharField(max_length=400, blank=True )
	date = models.DateTimeField(default=datetime.now)
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
	title = models.CharField(max_length=200, default = "Title") 
	ready = models.BooleanField(max_length=1500, blank=True)
	doc_specification = models.CharField(max_length=500, default = "Specification")
	doc_note = models.CharField(max_length=400, blank=True )
	doc_text = models.TextField(max_length=1500, default = "Text")
	date = models.DateTimeField(default=datetime.now)
	def __str__(self):
		return self.doc_note


#ET
class EventTypes(models.Model):  
	title = models.CharField(max_length=200, default = "Title") 
	ready = models.BooleanField(max_length=1500, blank=True)
	doc_note = models.CharField(max_length=400, blank=True )
	doc_text = models.TextField(max_length=1500, default = "Text")
	date = models.DateTimeField(default=datetime.now)	
	def __str__(self):
		return self.doc_note


#PC
class PayloadClasses(models.Model):
	title = models.CharField(max_length=200, default = "Title") 
	ready = models.BooleanField(max_length=1500, blank=True)
	doc_text = models.TextField(max_length=1500, default = "Text")
	date = models.DateTimeField(default=datetime.now)
	def __str__(self):
		return self.title


#DS
class DocSources(models.Model):  
	title = models.CharField(max_length=200, default = "Title") 
	ready = models.BooleanField(max_length=1500, blank=True)
	doc_note = models.CharField(max_length=400)
	doc_text = models.TextField(max_length=400,verbose_name='Текст')
	date = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('polls:DS')

	def data(self):
		return DocSources.objects.filter(id=self.id)










