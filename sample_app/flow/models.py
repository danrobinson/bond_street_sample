from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Step(models.Model):
    step_number = models.IntegerField(unique=True, db_index=True)

class CompletedStep(models.Model):
    user = models.ForeignKey(User)
    step = models.ForeignKey(Step)

# Create your models here.
