from fastapi import APIRouter
from random import randrange
from datetime import datetime

from Models.card import Card

router = APIRouter()

newDate = datetime.today().strftime('%d-%m-%Y %H:%I:%S')

dataCards = [{
    "id": 1,
    "title": "Nulis Blog",
    "description": "blog new journey with python (1)",
    "is_deleted" : False,
    "finished_at": "28-12-2022 18:34:59",
    "created_at": "28-12-2022 18:34:59",
    "updated_at": "28-12-2022 18:34:59",
    "deleted_at": "28-12-2022 18:34:59"},
    {
    "id": 2,
    "title": "Tugas kuliah KA1",
    "description": "blog new journey with python",
    "is_deleted" : False,
    "finished_at": "28-12-2022 18:34:59",
    "created_at": "28-12-2022 18:34:59",
    "updated_at": "28-12-2022 18:34:59",
    "deleted_at": "28-12-2022 18:34:59"
}]

# Get All
@router.get("/cards")
def get_cards():
    return {"data": dataCards}

# Create one Card
@router.post("/cards", status_code=status.HTTP_201_CREATED)
def create_card(card: Card):
    card_dict = card.dict()
    card_dict['id'] = randrange(0, 100)
    card_dict['created_at'] = newDate
    card_dict['is_deleted'] = False
    
    # print(card)
    dataCards.append(card_dict)
    return {"data": card_dict}

