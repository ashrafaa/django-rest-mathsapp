from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^exams/$', views.exam_list.as_view()),
    url(r'^exams/(?P<pk>[0-9]+)$', views.exam_detail.as_view()),
    url(r'^questions/$', views.question_list.as_view()),
    url(r'^questions/(?P<pk>[0-9]+)$', views.question_detail.as_view()),
    url(r'^answers/$', views.answer_list.as_view()),
    url(r'^answers/(?P<pk>[0-9]+)$', views.answer_detail.as_view()),
]