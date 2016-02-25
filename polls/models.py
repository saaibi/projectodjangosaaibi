import datetime
#from __future__ import unicode_literals
from django.utils import timezone
#from django.utils.encoding import python_2_unicode_compatible

from django.db import models


#@python_2_unicode_compatible
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.question_text
	def was_published_recently(self): 
	    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)	


#@python_2_unicode_compatible
class Choices(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choices_tex = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.choices_tex
