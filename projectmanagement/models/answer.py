from django.db import models
from .base import BaseModel
from .question import Question


class Answer(BaseModel):
    title = models.CharField(max_length=150)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, db_column='question_id', related_name='answers')
