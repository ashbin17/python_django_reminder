from django.db import models

# Create your models here.
class Reminder(models.Model):
    note = models.CharField(max_length=100)
    date = models.DateField()