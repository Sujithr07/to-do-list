from django.db import models
from django.contrib.auth.models import User 

class Todo(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.CharField(max_length=200)
    is_completed=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Todo: {self.content} | Completed: {self.is_completed}"

