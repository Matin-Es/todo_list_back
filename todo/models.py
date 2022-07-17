from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
