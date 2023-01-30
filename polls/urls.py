from django.urls import path

from . import views
from django.conf.urls import patterns, url
from polls import views

urlpatterns = url(r'^polls', 'polls.views.index', name='index'),
