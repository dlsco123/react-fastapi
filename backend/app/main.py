from fastapi import FastAPI
from .database import SessionLocal, engine, Base
from .models.member import User

# SQLAlchemy 모델의 Base 클래스를 사용해 테이블을 생성
Base.metadata.create_all(bind=engine)

# 요청마다 사용할 새로운 SQLAlchemy SessionLocal 인스턴스를 생성
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return {"Hello": "World"}