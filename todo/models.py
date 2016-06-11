from django.contrib.auth.models import User
from django.db import models

from .managers import ItemManager


class TodoList(models.Model):
    title = models.CharField(max_length=20)
    owner = models.ForeignKey(User, backref='lists')

class Item(models.Model):
    item_name = models.CharField(max_length=20)
    item_desc = models.CharField(max_length=500)
    is_done = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    list = models.ForeignKey(TodoList, backref="items")

    objects = ItemManager()
    default_manager = models.Manager()
