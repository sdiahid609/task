from django.db import models

class Task(models.Model):
    task = models.TextField()
    checkBox = models.BooleanField(default=False)

    def __str__(self):
        return self.task
