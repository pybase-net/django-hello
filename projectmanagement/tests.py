from django.test import TestCase
from .data.import_data import import_questions


# Create your tests here.
class UtilsTests(TestCase):
    def test_import_questions(self):
        error, questions = import_questions()
        if error:
            print(error)
        print(len(questions))
        self.assertGreater(len(questions), 0)
