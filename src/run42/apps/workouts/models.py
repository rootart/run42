from django.db import models
from django.utils.translation import ugettext as _

from interval.fields import IntervalField
from users.models import User


class Workout(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'))
    start_time = models.DateTimeField(_('Workout start time'),
        blank=True, null=True
    )
    end_time = models.DateTimeField(_('Workout finish time'),
        blank=True, null=True
    )
    duration = IntervalField(format='HMSX')
    distance = models.PositiveIntegerField(_('Distance'), blank=True, null=True)


    class Meta:
        verbose_name = _('Workout')
        verbose_name_plural = _('Workouts')

    def __unicode__(self):
        return str(self.duration)


class Lap(models.Model):
    workout = models.ForeignKey(Workout)
    distance = models.PositiveIntegerField(_('Lap disnace'))
    duration = IntervalField(format='HMSX')

    class Meta:
        verbose_name = _('Lap')
        verbose_name_plural = _('Laps')


    def __unicode__(self):
        return str(self.duration)
