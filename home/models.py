from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User


class ToDoModel(models.Model):
    work = models.TextField()
    auther = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)
    worker = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.work
