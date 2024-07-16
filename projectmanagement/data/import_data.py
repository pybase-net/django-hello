import json
from typing import Any, Dict, List, Tuple, Optional

import hello.settings
from projectmanagement.models import Question, Answer

PROJECT_MANAGEMENT_DATA_QUESTIONS = hello.settings.BASE_DIR / 'projectmanagement/data/questions.json'


class ImportData:
    def __init__(self, data_path: str = PROJECT_MANAGEMENT_DATA_QUESTIONS):
        self.data_path = data_path

    async def import_questions_async(self) -> Tuple[Optional[Exception], List[int]]:
        try:
            with open(self.data_path) as json_file:
                data = json.load(json_file)
                questions: List[Question] = []
                if len(data):
                    for row in data:
                        question = row['question']
                        q = await Question.objects.acreate(
                            title=question['title'],
                            difficult_level=question['difficultLevel'],
                            multiple_choices=question['multipleChoice'],
                        )
                        for answer in question['answers']:
                            await Answer.objects.acreate(
                                title=answer['title'],
                                correct=answer['correct'],
                                question=q
                            )
                        questions.append(q)
                return None, list(map(lambda q: q.id, questions))
        except Exception as e:
            return e, []
