import random

from django.db import transaction
from django.db.models import Prefetch, QuerySet
from typing import List, Tuple, Any

from projectmanagement.models import Question, Answer, Game, GameDetail, User

from projectmanagement.settings import NUMBER_OF_GAME_LEVEL_PER_QUESTIONS


def random_question_offset(limit: int, total_questions: int) -> (int, int):
    max_offset = max(total_questions - limit, 0) + 1
    offset = 0 if total_questions <= limit else random.randint(0, max_offset)
    return offset, offset + limit


class GameFactory:

    @staticmethod
    def find_game(game_id: int) -> tuple[Exception, Game, list[Question]]:
        try:
            game = Game.objects.get(id=game_id)
            # find questions
            game_details = GameDetail.objects.filter(
                game_id=game.id
            ).prefetch_related('question')
            questions = [gd.question for gd in game_details]
            return None, game, questions
        except Game.DoesNotExist:
            return Exception(f"Game {id} not found!"), None, []

    @staticmethod
    def start(user: User, level='default') -> tuple[None, Any, Any] | tuple[Exception, Game, list[Question]]:
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
        try:
            with transaction.atomic():
                # create new game
                game = Game.objects.create(user_id=user.id, question_count=questions.count())
                # create game details
                game_details = [GameDetail(game_id=game.id, question_id=q.id) for q in questions]
                GameDetail.objects.bulk_create(
                    game_details
                )
            return None, game, questions
        except Exception as e:
            return e, None, []
