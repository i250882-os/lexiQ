from django.db import models
from django.contrib.auth.models import User

# TODO what to do with same words with different meanings
class Word(models.Model):
    text = models.CharField(max_length=100)
    definition = models.TextField()
    example = models.TextField()

STATUS = [
    ('weak', 'weak'),
    ('known', 'known')
]
class UserWord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=10)
    # TODO add a score
    score = models.IntegerField()

class Paragraph(models.Model):
    text = models.TextField()
