from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .base import BaseModel


class TaggedItem(BaseModel):
    tag = models.SlugField()
    # hex color format : #ff0000
    color = models.CharField(max_length=7)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.tag

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
