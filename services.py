from models import Book
from sqlalchemy.orm import Session
from schemas import BookCreate

def create_book(db: Session, book: BookCreate):
    # db_book = Book(**book.dict())
    book_instance = Book(**book.model_dump())
    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)
    return book_instance

def get_book(db: Session):
    books = db.query(Book).all()
    return books
