from fastapi import APIRouter
from datetime import datetime

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

