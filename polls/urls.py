from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views, DS, TL, LOT, ET, PC

app_name = 'polls'
urlpatterns = [
	
	#polls/	
	url(r'^$', views.IndexView.as_view(), name='index'),

	#polls/login	
	url(r'^login/$', views.LoginView.as_view(), name='login'),
	

	#polls/register	
	url(r'^register/$', views.RegisterView.as_view(), name='register'),
	
	#polls/logout	
	url(r'^logout/$', views.LogoutView.as_view(), name='logout'),


				
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

				#polls/	LOT/2
				url(r'^LOT/(?P<pk>[0-9]+)/$', LOT.DetailView.as_view(), name='LOTDetail'),

				#polls/	LOT/Create
				url(r'^LOT/Create/$', LOT.LaunchOperationTypesCreate.as_view(), name='LOTCreate'),
				
				#polls/	LOT/2/Update
				url(r'^LOT/(?P<pk>[0-9]+)/Update/$', LOT.LaunchOperationTypesUpdate.as_view(), name='LOTUpdate'),
				
				#polls/	LOT/2/Delete
				url(r'^LOT/(?P<pk>[0-9]+)/Delete/$', LOT.LaunchOperationTypesDelete.as_view(), name='LOTDelete'),


	
				#polls/	ET/
				url(r'^ET/$', views.EventTypesOutput.as_view(), name='ET'),

				#polls/	ET/2
				url(r'^ET/(?P<pk>[0-9]+)/$', ET.DetailView.as_view(), name='ETDetail'),

				#polls/	ET/Create
				url(r'^ET/Create/$', ET.EventTypesCreate.as_view(), name='ETCreate'),
				
				#polls/	ET/2/Update
				url(r'^ET/(?P<pk>[0-9]+)/Update/$', ET.EventTypesUpdate.as_view(), name='ETUpdate'),
				
				#polls/	ET/2/Delete
				url(r'^ET/(?P<pk>[0-9]+)/Delete/$', ET.EventTypesDelete.as_view(), name='ETDelete'),
	


				#polls/	PC/
				url(r'^PC/$', views.PayloadClassesOutput.as_view(), name='PC'),
				
				#polls/	PC/2
				url(r'^PC/(?P<pk>[0-9]+)/$', PC.DetailView.as_view(), name='PCDetail'),

				#polls/	PC/Create
				url(r'^PC/Create/$', PC.PayloadClassesCreate.as_view(), name='PCCreate'),
				
				#polls/	PC/2/Update
				url(r'^PC/(?P<pk>[0-9]+)/Update/$', PC.PayloadClassesUpdate.as_view(), name='PCUpdate'),
				
				#polls/	PC/2/Delete
				url(r'^PC/(?P<pk>[0-9]+)/Delete/$', PC.PayloadClassesDelete.as_view(), name='PCDelete'),
]






