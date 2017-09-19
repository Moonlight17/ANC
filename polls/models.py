import datetime

from django.db import models
from django.utils import timezone




class Spisok(models.Model):
	doc_ready = models.BooleanField(max_length=1500)
	doc_TXT = models.BooleanField(max_length=1500)
	doc_title = models.CharField(max_length=200, default = "Title")
	doc_specification = models.CharField(max_length=500, default = "Specification")
	doc_note = models.CharField(max_length=400, blank=True )
	doc_text = models.CharField(max_length=1500, default = "Text")

	def __unicode__(self):
		return self.doc_title

class TitleList(models.Model):  
	title = models.ForeignKey('Spisok', on_delete=models.CASCADE) 
	doc_ready = models.BooleanField(max_length=1500)
	doc_TXT = models.BooleanField(max_length=1500)
	doc_title = models.CharField(max_length=200, default = "Title")
	doc_specification = models.CharField(max_length=500, default = "Specification")
	doc_note = models.CharField(max_length=400, blank=True )
	doc_text = models.CharField(max_length=1500, default = "Text")

	def __unicode__(self):
		return self.doc_title





def __str__(self):
	return self.doc_title