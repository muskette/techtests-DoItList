from django.db import models


class ItemManager(models.Manager):
    def get_queryset(self):
        qs = super(ItemManager, self).get_queryset()
        qs = qs.filter(deleted=False)
        return qs

    def unfinished(self):
        qs = self.get_queryset()
        qs = qs.filter(is_done=False)
        return qs

    def get_all(self):
        return super(ItemManager, self).get_queryset()
