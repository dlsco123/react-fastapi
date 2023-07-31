from sqlalchemy import Boolean, Column, Integer, String
from ..database import Base

class User(Base):
    __tablename__ = "member"

    email = Column(String(50), primary_key=True, index=True)
    pwd = Column(String(50))
    nickname = Column(String(50))
    gender = Column(String(1))
    name = Column(String(50))
    auth = Column(Integer)
    contact = Column(String(255))
    birth = Column(String(50))
    coin = Column(Integer)
    profile = Column(String(100))
