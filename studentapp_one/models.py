from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=64, null=True)
    address = models.TextField(null=True)
    dob = models.DateTimeField(null=True, blank=True)
    roll = models.CharField(max_length=64, null=False, unique=True)
    marks = JSONField(default=dict)

    def __str__(self):
        return str(self.name)
