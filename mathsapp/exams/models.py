from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

class Exam(models.Model):
    name = models.CharField(max_length=30)
    pass_percentage = models.IntegerField(
        default=80,
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    ) # expected value: 0 - 100
    date_created = models.DateTimeField(auto_now_add=True, blank=True) 

    def get_exam_pass(self):
        return "Exam [%s] has %d passing percentage." % (self.name, self.pass_percentage) 

    def __str__(self):
        return self.name + " is added."

class Question(models.Model):
    DIFFICULTY_LEVELS = (
        ('VH', 'Very Hard'),
        ('HA', 'Hard'),
        ('ME', 'Medium'),
        ('EA', 'Easy'),
        ('VE', 'Very Easy')
    )

    text = models.CharField(max_length=255)
    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_LEVELS,
        default='ME'
    ) # value: 1 (very easy) to 5 (very hard)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.text + " is added."

class Answer(models.Model):
    SOLUTION_VALUE = (
        ('CO', 'Correct'),
        ('AC', 'Acceptable'),
        ('WR', 'Wrong')
    )

    text = models.CharField(max_length=255)
    solution_value = models.CharField(
        max_length=10,
        choices=SOLUTION_VALUE,
        default='WR'
    ) # value: 0 (total wrong), 1 (not exact), 2 (correct)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Answer: %s (%s)" % (self.text, self.solution_value)

