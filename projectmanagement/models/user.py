from django.db import models
from .base import BaseModel
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, BaseModel):
    pass
