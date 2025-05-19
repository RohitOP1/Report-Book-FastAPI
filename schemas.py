from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    description: str
    year: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        # For Pydantic <2.x, use orm_mode
        # orm_mode = True  

        # For Pydantic 2.x+
        from_attributes = True
