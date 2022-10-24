from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.new_questions, name="main"),
    re_path(r'^login/$', views.test, name="test"),
    re_path(r'^signup/$', views.test, name="test"),
    re_path(r'^question/(?P<id>\d+)/$', views.question, name="question"),
    re_path(r'^ask/$', views.test, name="test"),
    re_path(r'^popular/$', views.popular, name="popular questions"),
    re_path(r'^new/$', views.test, name="test"),
]