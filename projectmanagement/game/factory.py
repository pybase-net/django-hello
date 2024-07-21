import random

from django.db.models import Prefetch

from projectmanagement.models import Question, Answer

from projectmanagement.settings import NUMBER_OF_GAME_LEVEL_PER_QUESTIONS


def random_question_offset(limit: int, total_questions: int) -> (int, int):
    max_offset = max(total_questions - limit, 0) + 1
    offset = 0 if total_questions <= limit else random.randint(0, max_offset)
    return offset, offset + limit


class GameFactory:

    @staticmethod
    def start(level='default'):
        """
        Step 1: Random question OFFSET <=> OFFSET + LIMIT <= COUNTOFQUESTION
        Step 2: Create Game with selected questions
        """
        limit = NUMBER_OF_GAME_LEVEL_PER_QUESTIONS[level]
        if level != 'default':
            total_questions = Question.objects.filter(difficult_level=Question.DIFFICULT_LEVELS[level]).count()
            start, end = random_question_offset(limit=limit, total_questions=total_questions)
            questions = Question.objects.filter(difficult_level=Question.DIFFICULT_LEVELS[level])[start:end]
        else:
            total_questions = Question.objects.count()
            start, end = random_question_offset(limit=limit, total_questions=total_questions)
            questions = Question.objects.filter()[start:end]
        questions.prefetch_related(Prefetch("answer", queryset=Answer.objects.all()))
        return questions
