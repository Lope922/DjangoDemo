from django.conf.urls import url 
from . import views


#post_list identifies the name of the url that will be usedd to identify the view
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
]