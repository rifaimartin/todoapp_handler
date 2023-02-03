
# find by ID Card
def find_by(id, dataCards):
    for p in dataCards:
        if p["id"] == id:
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