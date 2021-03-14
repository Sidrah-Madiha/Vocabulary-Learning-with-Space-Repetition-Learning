## This is a simple backackend project ,using Django and MongDB
In this project Tried my hands on Django +MongoDB using Djongo

-  It contains 2 apps: cards and decks
- A deck can contain many cards, cards can only belong to a specific  deck, so I added foreign key for it.
- Used Djongo to map django model fields to noSQL mongoDB.
- Created these api endpoints:
    `cards/` to fetch all cards
    `decks/` to fetch deck and all cards within decks
    `decks/:id/cards` to fetch cards related to only a specific deck
    `cards/?question_type=` to filter cards based on field `question_type`
    `cards/?ordering=` to order cards based on field `question_type` and default ordering based on `question`
    `cards/?search=` to search cards based on `question` and `answer` field
  

Thanks @gwenf for the amazing tutorial for understanding this tech stack.