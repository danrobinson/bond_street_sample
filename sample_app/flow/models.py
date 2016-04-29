from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Step(models.Model):
    number = models.IntegerField(primary_key=True)

    class Meta:
        ordering = ["number"]

    def __unicode__(self):
        return "Step " + str(self.number)

    def get_absolute_url(self):
        return reverse("step", args=(self.number,))


class UserStep(models.Model):
    user = models.ForeignKey(User)
    step = models.ForeignKey(Step)
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        result = unicode(self.user) + "'s " + unicode(self.step)
        result += " (" + ("completed" if self.completed else "incomplete") + ")"
        return result

    def get_absolute_url(self):
        return self.step.get_absolute_url()