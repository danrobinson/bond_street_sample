from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Step(models.Model):
    """Model for a single step."""
    number = models.IntegerField(primary_key=True)

    class Meta:
        ordering = ["number"]

    def __unicode__(self):
        return "Step " + str(self.number)


class UserStep(models.Model):
    """Model for a single user's progress on a particular step."""
    user = models.ForeignKey(User)
    step = models.ForeignKey(Step)
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        result = unicode(self.user) + "'s " + unicode(self.step)
        parenthetical = ("completed" if self.completed else "incomplete")
        result += " (" + parenthetical + ")"
        return result

    def get_absolute_url(self):
        return reverse("flow_step", args=(self.step.number,))
