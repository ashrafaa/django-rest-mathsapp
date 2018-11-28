from django.conf.urls import url, include
from django.contrib import admin
from .exams import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^exams/$', views.exam_list),
    url(r'^exams/(?P<pk>[0-9]+)$', views.exam_detail),
    url(r'^questions/$', views.question_list.as_view()),
    url(r'^questions/(?P<pk>[0-9]+)$', views.question_detail.as_view()),
    url(r'^answers/$', views.answer_list.as_view()),
    url(r'^answers/(?P<pk>[0-9]+)$', views.answer_detail.as_view()),
]
