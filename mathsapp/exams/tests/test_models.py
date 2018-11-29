from django.test import TestCase
from ..models import Exam, Question, Answer

class ModelCreationTest(TestCase):
    def setUp(self):
        spring_midterm_exam = Exam.objects.create(
            name='Spring Midterm', pass_percentage=70)
        spring_final_exam = Exam.objects.create(
            name='Spring Final', pass_percentage=80)
        prime_question = Question.objects.create(
            text='What are all the prime numbers between 20 and 30?', difficulty='ME', exam=spring_midterm_exam)
        fraction_question = Question.objects.create(
            text='What is 0.3 as a fraction?', difficulty='EA', exam=spring_final_exam)
        prime_right_answer = Answer.objects.create(
            text='29', solution_value='CO', question=prime_question)
        prime_wrong_answer = Answer.objects.create(
            text='27', solution_value='WR', question=prime_question)
            
    def test_exam(self):
        spring_midterm = Exam.objects.get(name='Spring Midterm')
        spring_final = Exam.objects.get(pass_percentage=80)

        self.assertEqual(
            spring_midterm.get_exam_pass(), 'Exam [Spring Midterm] has 70 passing percentage.')
        self.assertEqual(
            spring_final.get_exam_pass(), 'Exam [Spring Final] has 80 passing percentage.')

    def test_question(self):
        prime = Question.objects.get(difficulty='ME')
        fraction = Question.objects.get(text='What is 0.3 as a fraction?')

        self.assertEqual(
            prime.get_question_level(), 'Question [What are all the prime numbers between 20 and 30?] has ME level.')
        self.assertEqual(
            fraction.get_question_level(), 'Question [What is 0.3 as a fraction?] has EA level.')

    def test_answer(self):
        correct = Answer.objects.get(text='29')
        wrong = Answer.objects.get(solution_value='WR')

        self.assertEqual(
            correct.get_answer_value(), 'Answer [29] is CO.')
        self.assertEqual(
            wrong.get_answer_value(), 'Answer [27] is WR.')
