from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=20, blank=True)
    memo = models.TextField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    Tday = models.BooleanField(default=False, blank=True)
    Fday = models.BooleanField(default=False, blank=True)
    numDay = models.BooleanField(default=False, blank=True)
    important = models.BooleanField(default=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title
