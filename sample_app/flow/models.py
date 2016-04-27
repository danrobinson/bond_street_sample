from django.db import models
from django.contrib.auth.models import User


class Step(models.Model):
    step_number = models.IntegerField(unique=True, db_index=True)

    class Meta:
        ordering = ['step_number']

    def __unicode__(self):
        return "Step " + str(self.step_number)


class CompletedStep(models.Model):
    user = models.ForeignKey(User)
    step = models.ForeignKey(Step)
