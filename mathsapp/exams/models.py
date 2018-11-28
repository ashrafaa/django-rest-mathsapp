from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Exam(models.Model):
    name = models.CharField(max_length=30)
    passPercentage = models.IntegerField(
        default=80,
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    ) # expected value: 0 - 100

    def __str__(self):
        return self.name

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

    def __str__(self):
        return "Question: %s (%s)" % (self.text, self.difficulty)

class Answer(models.Model):
    SOLUTION_VALUE = (
        ('CO', 'Correct'),
        ('AC', 'Acceptable'),
        ('WR', 'Wrong')
    )

    text = models.CharField(max_length=255)
    solutionValue = models.CharField(
        max_length=10,
        choices=SOLUTION_VALUE,
        default='WR'
    ) # value: 0 (total wrong), 1 (not exact), 2 (correct)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return "Answer: %s (%s)" % (self.text, self.solutionValue)

