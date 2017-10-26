from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views, DS, TL

app_name = 'polls'
urlpatterns = [
	
	#polls/	
	url(r'^$', views.IndexView.as_view(), name='index'),
	
	#polls/	DS/
	url(r'^DS/$', views.DocSourcesOutput.as_view(), name='DS'),
	
	#polls/	DS/2
	url(r'^DS/(?P<pk>[0-9]+)/$', DS.DetailView.as_view(), name='DSDetail'),

	#polls/	DS/Create
	url(r'^DS/Create/$', DS.DocSourcesCreate.as_view(), name='DSCreate'),
	
	#polls/	DS/2/Update
	url(r'^DS/(?P<pk>[0-9]+)/Update/$', DS.DocSourcesUpdate.as_view(), name='DSUpdate'),
	
	#polls/	DS/2/Delete
	url(r'^DS/(?P<pk>[0-9]+)/Delete/$', DS.DocSourcesDelete.as_view(), name='DSDelete'),


	
	#polls/	TL/
	url(r'^TL/$', views.TitleListOutput.as_view(), name='TL'),

	#polls/	TL/2
	url(r'^TL/(?P<pk>[0-9]+)/$', TL.DetailView.as_view(), name='TLDetail'),

	#polls/	TL/Create
	url(r'^TL/Create/$', TL.TitleListCreate.as_view(), name='TLCreate'),
	
	#polls/	TL/2/Update
	url(r'^TL/(?P<pk>[0-9]+)/Update/$', TL.TitleListUpdate.as_view(), name='TLUpdate'),
	
	#polls/	TL/2/Delete
	url(r'^TL/(?P<pk>[0-9]+)/Delete/$', TL.TitleListDelete.as_view(), name='TLDelete'),


	
	#polls/	LOT/
	url(r'^LOT/$', views.LaunchOperationTypesOutput.as_view(), name='LOT'),


	
	#polls/	ET/
	url(r'^ET/$', views.EventTypesOutput.as_view(), name='ET'),
	


	#polls/	PC/
	url(r'^PC/$', views.PayloadClassesOutput.as_view(), name='PC'),
]






