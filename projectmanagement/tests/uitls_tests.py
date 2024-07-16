from django.test import TestCase
from asgiref.sync import async_to_sync
from ..data.import_data import ImportData


class UtilsTests(TestCase):
    def setUp(self) -> None:
        self.import_data = ImportData()

    def test_import_questions(self):
        # Ensure to call the async method correctly
        error, questions = async_to_sync(self.import_data.import_questions_async)()
        if error:
            print(f"Error: {error}")
        else:
            print(f"Number of imported questions: {len(questions)}")

        self.assertGreater(len(questions), 0)
