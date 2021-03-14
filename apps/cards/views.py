from django.shortcuts import render
from rest_framework import serializers, viewsets
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Card

# Create your views here.
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class CardsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    filter_backends = (filters.DjangoFilterBackend,SearchFilter, OrderingFilter)
    filterset_fields = ['question_type']
    search_fields = ['question', 'answer']
    ordering_fields = ['question_type']
    ordering = ['question']