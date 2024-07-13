from django.db import models
from .base import BaseModel


class Question(BaseModel):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'
    DIFFICULT_LEVELS = {
        EASY: EASY,
        MEDIUM: MEDIUM,
        HARD: HARD,
    }
    title = models.CharField(max_length=200)
    difficult_level = models.CharField(
        max_length=10,
        choices=DIFFICULT_LEVELS
    )
    multiple_choices = models.BooleanField(default=False)
