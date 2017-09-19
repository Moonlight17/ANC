from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^add/$', views.text_new, name='add'),
	url(r'^(?P<spisok_id>[0-9]+)/edit/$', views.text_edit, name='edit'),
	url(r'^(?P<spisok_id>[0-9]+)/delete/$', views.text_delete, name='delete'),
]