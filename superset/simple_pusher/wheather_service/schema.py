# build a schema using pydantic
from pydantic import BaseModel


class Whether(BaseModel):
    city: str
    temp: int

    class Config:
        orm_mode = True