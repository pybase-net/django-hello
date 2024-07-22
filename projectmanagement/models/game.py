from django.db import models
from .base import BaseModel
from .user import User
from django.utils import timezone


class Game(BaseModel):
    total_point = models.IntegerField(null=True, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    question_count = models.IntegerField(null=True, default=0)
    correct_answer_count = models.IntegerField(null=True, default=0)
    started_at = models.DateTimeField(null=True)
    ended_at = models.DateTimeField(null=True)

    @property
    def started(self):
        return self.started_at is not None

    def get_questions(self):
        return [detail.question for detail in self.details.all()]

    def __calculate_total_time(self):
        """
        Business rule:
        - Each easy question: 30 seconds
        - Each medium question: 1 minutes
        - Each hard question: 2.5 minutes
        """
        questions = self.get_questions()
        total_time = 0
        for q in questions:
            total_time += q.time_allocation
        return total_time

    @property
    def remaining_time(self):
        if self.ended_at is not None:
            return 0
        total_time = self.__calculate_total_time()
        if self.started_at is not None:
            elapsed_time = timezone.now() - self.started_at
            return int(max(0, total_time - elapsed_time.total_seconds()))
        return 0
