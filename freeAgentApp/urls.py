from django.conf.urls import url
from . import views

app_name='freeAgentApp'

urlpatterns = [
    
    #/freeAgentApp/
    url(r'^$', views.index, name='index'),
    #/freeAgentApp/13/
    url(r'^(?P<project_id>[0-9]+)/$',views.detail, name='detail'),
]