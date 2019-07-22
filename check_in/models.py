from django.db import models

class Users(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)