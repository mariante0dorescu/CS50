from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
from django.urls import reverse

# Create your tests here.

class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        #returns Flase for questions whose pub date is older than 1 day
        time = timezone.now() - datetime.timedelta(days=1, seconds = 1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        #returns true for questions whose pub_date is within the last day
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def createQuestion(question_text, days):
    #create a question with a number of days offset to now (negative fro q published in the past, positive for the one not yet published)

    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text = question_text, pub_date = time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        #if no questions, an appropiate message is displayed
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_questions_list"],[])

    def test_past_questions(self):
        "questions with a pub date in the past are displayed on the index page"
        question = createQuestion(question_text = "Past questions", days = -30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_questions_list"], [question])
    
    def test_future_question(self):
        #question with a pub date in the future is not displayed on the index page
        question = createQuestion(question_text = "Past questions", days = 30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_questions_list"], [])  
    
    def test_future_past_questions(self):
        "even past and future questions exists only past is displayed"
        question_past = createQuestion(question_text = "Past questions", days = -30)
        question_future = createQuestion(question_text = "Past questions", days = 30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_questions_list"], [question_past])
    
    def test_two_past_question(self):
        #question with a pub date in the future is not displayed on the index page
        question1 = createQuestion(question_text = "Past question 1", days = -30)
        question2 = createQuestion(question_text = "Past question 2", days = -5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_questions_list"], [question2, question1])

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):    
    #the detail view of a question with a pub_date in the future returns a 404
        future_question = createQuestion(question_text="Future question", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = createQuestion(question_text="Past question", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, past_question.question_text)