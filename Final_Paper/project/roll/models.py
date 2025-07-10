# roll/models.py
from django.db import models

class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=70)
    stuemail = models.EmailField()
    sturesult = models.TextField()

    def __str__(self):
        return self.stuname
