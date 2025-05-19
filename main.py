from fastapi import FastAPI, Depends, HTTPException
import services, models, schemas
from db import get_db, engine
from sqlalchemy.orm import Session

# Create database tables on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API!"}

@app.get("/books", response_model=list[schemas.Book])
def get_all_books(db: Session = Depends(get_db)):
    books = services.get_book(db)
    return books

@app.post("/books", response_model=schemas.Book)
def create_new_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return services.create_book(db, book)