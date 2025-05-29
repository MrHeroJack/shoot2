from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True # 从 from_attributes = True 更改而来，以兼容 Pydantic v1
