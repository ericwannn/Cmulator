import datetime
from django.utils import timezone
from django.db import models


class SimulationConfig(models.Model):

    AUTHOR_CHOICES = [
        ('eva_chen', 'Eva'),
        ('conan_zhang', 'Conan'),
        ('freya_meng', 'meng'),
        ('eric_wan', 'Eric'),
    ]
    sim_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30, choices=AUTHOR_CHOICES)
    date = models.DateTimeField()

    class Meta:
        ordering = ['date']
        verbose_name = 'job'
        verbose_name_plural = 'jobs'


class SimulationResult(models.Model):
    settings = models.ForeignKey(SimulationConfig, on_delete=models.CASCADE)
    sharpe = models.FloatField()
    vol = models.FloatField()
    turnover = models.FloatField()
    ret = models.FloatField()
    date = models.DateTimeField()

    class Meta:
        ordering = ['date']
        verbose_name = 'result'
        verbose_name_plural = 'results'


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
