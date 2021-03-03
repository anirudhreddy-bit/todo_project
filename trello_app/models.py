from django.db import models
from django.utils import timezone

class TaskList(models.Model):
    name=models.CharField(max_length=50)
    created_at = models.DateTimeField(
        default=timezone.now()
    )

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    dsc = models.TextField()
    created_at = models.DateTimeField()
    due_date = models.DateTimeField()
    list=models.ForeignKey(TaskList,on_delete=models.CASCADE)