from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Deck
from apps.cards.views import CardSerializer
from apps.cards.models import Card
from rest_framework.response import Response

# Create your views here.
class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'

class DecksViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = DeckSerializer
    queryset = Deck.objects.all()

class DeckCardsViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

    def list(self, request, deck_pk):
        card = Card.objects.filter(deck=deck_pk)
        serializer = self.get_serializer(card, many=True)
        return Response(serializer.data)