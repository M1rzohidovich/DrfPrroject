from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


