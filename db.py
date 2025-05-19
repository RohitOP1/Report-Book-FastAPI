from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Correct URL-encoded password (@ becomes %40)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Yoyorp%401@localhost:5432/recordbook"

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for your ORM models
Base = declarative_base()

# Dependency for getting a DB session in FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Optional: Call this to create all tables
def create_table():
    Base.metadata.create_all(bind=engine)
