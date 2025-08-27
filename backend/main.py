from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, models
from database import SessionLocal, engine

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/signup")
def signup(username: str, email: str, password: str, db: Session = Depends(get_db)):
    # Manually build the schema object
    from schemas import UserCreate
    user = UserCreate(username=username, email=email, password=password)
    return crud.create_user(db=db, user=user)


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

