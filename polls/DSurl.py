from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views, DS, TL

app_name = 'polls'
urlpatterns = [
	#polls/	DS/
	url(r'^/$', views.DocSourcesOutput.as_view(), name='DS'),
	
	#polls/	DS/2
	url(r'^/(?P<pk>[0-9]+)/$', DS.DetailView.as_view(), name='DSDetail'),

	#polls/	DS/Create
	url(r'^/Create/$', DS.DocSourcesCreate.as_view(), name='DSCreate'),
	
	#polls/	DS/2/Update
	url(r'^/(?P<pk>[0-9]+)/Update/$', DS.DocSourcesUpdate.as_view(), name='DSUpdate'),
	
	#polls/	DS/2/Delete
	url(r'^/(?P<pk>[0-9]+)/Delete/$', DS.DocSourcesDelete.as_view(), name='DSDelete'),
	]