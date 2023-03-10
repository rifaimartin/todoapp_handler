from fastapi import APIRouter, Response, HTTPException, status
from random import randrange
from datetime import datetime, timezone

from Models.card import Card
from Services import cardService
router = APIRouter()

# datetime.now(timezone.utc)
newDate = datetime.today().strftime('%d-%m-%Y %H:%I:%S')

dataCards = [{
    "id": 1,
    "title": "Nulis Blog",
    "description": "blog new journey with python (1)",
    "is_deleted" : False,
    'status' : 'TODO',
    "finished_at": "28-12-2022 18:34:59",
    "created_at": "28-12-2022 18:34:59",
    "updated_at": "28-12-2022 18:34:59",
    "deleted_at": "28-12-2022 18:34:59"},
    {
    "id": 2,
    "title": "Tugas kuliah KA1",
    "description": "blog new journey with python",
    "is_deleted" : False,
    'status' : 'TODO',
    "finished_at": "28-12-2022 18:34:59",
    "created_at": "28-12-2022 18:34:59",
    "updated_at": "28-12-2022 18:34:59",
    "deleted_at": "28-12-2022 18:34:59"
}]


# Get All
@router.get("/cards")
def get_cards():
    retrievedDataCards = cardService.getAllByIsdeleted(dataCards)
    return {"data": retrievedDataCards}

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

# Get One Card by ID
@router.get("/cards/{id}")
def get_card(id: int, response: Response):
    
    card = cardService.find_by(id, dataCards)
    if not card:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Card with the id: {id} was not found")
    return {"data": card}

# Delete one Card by ID
@router.delete("/cards/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cardt(id: int):
    index = cardService.find_index_cards(id, dataCards)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Card with the id: {id} was not found")
    card = cardService.find_by(id, dataCards)

    #how descruturing object with pyhton?
    print("data card",card['title'])
    print("index", index)
    
    cardUpdate = Card(id=card['id'],title=card['title'],description=card['description'],is_deleted=True,created_at=card['created_at'],updated_at=card['updated_at'],deleted_at=newDate,finished_at=card['finished_at'])
    dataCards[index].update(cardUpdate.dict())
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/cards/{id}")
def update_card(id: int, card: Card):
    index = cardService.find_index_cards(id, dataCards)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Card with the id: {id} was not found")
    retrivedCard = cardService.find_by(id, dataCards)
        
    card_dict = card.dict()
    card_dict['id'] = id
    card_dict['updated_at'] = newDate
    card_dict['created_at'] = retrivedCard['created_at']
    dataCards[index].update(card_dict) 
    return {"data": card_dict}


@router.put("/cards/status/{id}")
def update_card(id: int):
    index = cardService.find_index_cards(id, dataCards)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Card with the id: {id} was not found")
    card = cardService.find_by(id, dataCards)
    
    cardUpdate = Card(id=card['id'],title=card['title'],description=card['description'],is_deleted=card['is_deleted'],status='DONE',created_at=card['created_at'],updated_at=card['updated_at'],finished_at=newDate)
    
    dataCards[index].update(cardUpdate.dict()) 
    return {"data": dataCards[index]}

