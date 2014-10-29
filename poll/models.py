import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)
    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean=True
    was_published_recently.short_description='Published recently?'
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

class Choice(models.Model):
    def __unicode__(self):
        return self.choice_text
    question=models.ForeignKey(Question)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

class Reporter(models.Model):
    full_name=models.CharField(max_length=70)

    def __unicode__(self):
        return self.full_name

class Article(models.Model):
    pub_date=models.DateField()
    headline=models.CharField(max_length=200)
    content=models.TextField()
    reporter=models.ForeignKey(Reporter)

    def __str__(self):
        return self.headline
