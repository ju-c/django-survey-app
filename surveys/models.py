from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model

# The survey model that represent each survey
class Survey(models.Model):
    title = models.CharField(max_length=255)
    creator = models.ForeignKey(
            get_user_model(),
            on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('survey_edit', args=[str(self.id)])

# The question model for each question of the survey
class Question(models.Model):
    survey = models.ForeignKey(
            Survey,
            on_delete=models.CASCADE,
            related_name='questions',
    )
    quest = models.CharField(max_length=255)

    def __str__(self):
        return self.quest

# The option model for the multi-choice answer options
class Option(models.Model):
    question = models.ForeignKey(
            Question,
            on_delete=models.CASCADE,
            related_name='options'
    )
    choice = models.CharField(max_length=255)

    def __str__(self):
        return self.choice

class Submission(models.Model):
    survey = models.ForeignKey(
            Survey,
            on_delete=models.CASCADE,)
    create_at = models.DateTimeField(default=timezone.now)
    is_complete = models.BooleanField(default=False)

class Answer(models.Model):
    submission = models.ForeignKey(
            Submission,
            on_delete=models.CASCADE
    )
    option = models.ForeignKey(
            Option,
            on_delete=models.CASCADE
    )
