from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import crud, schemas, models

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency: DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import Query

# --- Signup Route (Query Parameters) ---
@app.post("/signup", response_model=schemas.UserResponse)
def signup(
    username: str = Query(...),
    email: str = Query(...),
    password: str = Query(...),
    db: Session = Depends(get_db)
):
    # Check if user already exists
    db_user = db.query(models.User).filter(models.User.email == email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create UserCreate schema manually
    user_data = schemas.UserCreate(username=username, email=email, password=password)

    return crud.create_user(db=db, user=user_data)




@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }
