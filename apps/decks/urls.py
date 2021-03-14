from rest_framework_nested import routers
from .views import (DecksViewSet, DeckCardsViewSet)
from django.urls import path, include

router = routers.SimpleRouter()

router.register('', DecksViewSet)
cards_router = routers.NestedSimpleRouter(router, '', lookup='deck')
cards_router.register('cards', DeckCardsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(cards_router.urls)),
]