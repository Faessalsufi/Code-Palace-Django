from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10000)
    content = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} - Question'

    def get_absolute_url(self):
        return reverse("CodePalaceBase:questions_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    question = models.ForeignKey(
        Question, related_name="comment", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.question.title, self.question.user)

    def get_absolute_url(self):
        return reverse("CodePalaceBase:question_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
