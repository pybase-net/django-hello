from django.db import models
from .base import BaseModel
from .user import User


class GameRank(BaseModel):
    totalQuestionCount = models.IntegerField(default=0)
    totalAnswerCount = models.IntegerField(default=0)
    totalPoint = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)  # New rank field
