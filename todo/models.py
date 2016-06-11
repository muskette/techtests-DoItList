from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.db import models

from .managers import ItemManager


class TodoList(models.Model):
    title = models.CharField(max_length=20)
    owner = models.ForeignKey(User, related_name='lists')

    @property
    def get_absolute_url(self):
        return reverse_lazy('todo:list', self.pk)

class Item(models.Model):
    item_name = models.CharField(max_length=20)
    item_desc = models.CharField(max_length=500)
    is_done = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    list = models.ForeignKey(TodoList, related_name="items")

    objects = ItemManager()
    default_manager = models.Manager()
