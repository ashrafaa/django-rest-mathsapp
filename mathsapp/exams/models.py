from django.db import models

class Exam(models.Model):
    name = models.CharField(max_length=30)
    passPercentage = models.FloatField() # expected value: 0 - 100

    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.CharField(max_length=255)
    difficulty = models.IntegerField() # value: 1 (very easy) to 5 (very hard)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return "Question: %s (%d)" % (self.text, self.difficulty)

class Answer(models.Model):
    text = models.CharField(max_length=255)
    solutionValue = models.IntegerField() # value: 0 (total wrong), 1 (not exact), 2 (correct)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return "Answer: %s (%d)" % (self.text, self.solutionValue)

