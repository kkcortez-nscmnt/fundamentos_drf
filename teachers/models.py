from django.db import models


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.name
