from django.conf.urls import patterns,url
from fb_chatBot import views
from .views import MyQuoteBotView


urlpatterns = patterns('',
	url(r'^$', views.index,name = 'index'),
	url(r'^facebook_auth/?$', MyQuoteBotView.as_view()))