from .models import Exam, Question, Answer
from rest_framework import serializers

class ExamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exam
        fields = ('name', 'passPercentage', 'question')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('text', 'difficulty', 'answer')

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('text', 'solutionValue')