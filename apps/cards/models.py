from django.db import models

from apps.decks.models import Deck
# Create your models here.
class Card(models.Model):

    class QuestionType(models.IntegerChoices):
        multiple_choice = 0
        open_ended = 1

    question = models.CharField(max_length=255)
    answer = models.TextField()
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    question_type = models.IntegerField(choices=QuestionType.choices, default=1)

    def __str__(self):
        return self.question