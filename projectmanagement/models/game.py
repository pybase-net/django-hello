from django.db import models
from .base import BaseModel
from .user import User


class Game(BaseModel):
    total_point = models.IntegerField(null=True, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    question_count = models.IntegerField(null=True, default=0)
    correct_answer_count = models.IntegerField(null=True, default=0)
