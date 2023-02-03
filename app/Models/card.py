from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Card(BaseModel): 
    id: int = None
    title: str = None
    description: Optional[str] = None
    is_deleted: bool = False
    created_at: str = None 
    updated_at: str = None
    deleted_at: str = None
    finished_at: str = None