from .models import Exam, Question, Answer
from rest_framework import serializers

class ExamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exam
        fields = ('name', 'passPercentage')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    exam = ExamSerializer()

    class Meta:
        model = Question
        fields = ('text', 'difficulty', 'exam')

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Answer
        fields = ('text', 'solutionValue', 'question')