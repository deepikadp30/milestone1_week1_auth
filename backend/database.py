# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Update with your MySQL username, password, host, and database name
DATABASE_URL = "mysql+mysqlconnector://root:p1808adminprasath@localhost:3306/text_morph_db"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
