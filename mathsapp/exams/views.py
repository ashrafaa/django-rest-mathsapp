from rest_framework import status, generics
from .models import Exam, Question, Answer
from .serializers import *

class answer_list(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class answer_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class question_list(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class question_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class =  QuestionSerializer

class exam_list(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class exam_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class =  ExamSerializer