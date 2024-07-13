from django.db import models
from .base import BaseModel
from .question import Question
from .answer import Answer
from .game import Game


class GameDetail(BaseModel):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    correct = models.BooleanField(default=False)

    class Meta:
        # unique_together = [["game", "question", "answer"]] => will be deprecated soon
        constraints = [
            models.UniqueConstraint(fields=['game', 'question', 'answer'], name='unique_game_question_answer')
        ]
