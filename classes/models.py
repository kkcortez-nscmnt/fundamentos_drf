from django.db import models


class Class(models.Model):
    cls_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    field = models.CharField(max_length=50)

    def __str__(self):
        return self.name
