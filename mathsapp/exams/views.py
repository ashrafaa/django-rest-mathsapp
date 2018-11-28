from rest_framework import status, generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Exam, Question, Answer
from .serializers import *

class answer_list(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('question__text', 'solutionValue')

class answer_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class question_list(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('exam__name', 'difficulty')

class question_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class =  QuestionSerializer

class exam_list(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'passPercentage')

class exam_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class =  ExamSerializer
