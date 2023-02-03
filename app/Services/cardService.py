
# find by ID Card
def find_by(id, dataCards):
    for p in dataCards:
        if p["id"] == id and p["is_deleted"] == False:
            return p
        
# # find index by id        
# def find_index_from_card(id, dataCards):
#     for i, p in enumerate(dataCards):
#         if p['id'] == id:
#             return i
        
# find index by id                
def find_index_cards(id, dataCards):
    card = find_by(id, dataCards)
    if not card:
        return None
    return dataCards.index(card)

def getAllByIsdeleted(dataCards):
    filterDataCards = (card for card in dataCards if card['is_deleted']==False)

    return filterDataCards
