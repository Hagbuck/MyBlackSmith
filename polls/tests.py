import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_futur_question(self):
        time = timezone.now() + datetime.timedelta(days = 30)
        futur_question = Question(pub_date = time)

        self.assertIs(futur_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days = 1, seconds = 1)
        futur_question = Question(pub_date = time)

        self.assertIs(futur_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours = 23, minutes = 59, seconds = 59)
        futur_question = Question(pub_date = time)

        self.assertIs(futur_question.was_published_recently(), True)