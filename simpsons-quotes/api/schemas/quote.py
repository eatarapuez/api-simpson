from pydantic import BaseModel
from typing import Optional

class Quote(BaseModel):
    id: Optional[str]
    quote: str
    class Config:
        orm_mode = True