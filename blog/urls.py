from django.conf.urls import url 
from . import views 

#this defines the pattern that the url will have based on primary keys assigned through the database.
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
