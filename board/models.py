from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category =  models.CharField(primary_key = True, max_length=20)
    color = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category}"

class Task(models.Model):
    name = models.CharField(primary_key = True, max_length=50)
    description = models.CharField(max_length=200)
    due_date = models.DateTimeField("time task is due")
    user_on_task = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"for {self.user.username} is: {self.name}"