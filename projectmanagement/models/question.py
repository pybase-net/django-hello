from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from .base import BaseModel
from .tagged_item import TaggedItem


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
    tags = GenericRelation(TaggedItem)

    def __str__(self):
        return f'{self.title} ({self.difficult_level})'
