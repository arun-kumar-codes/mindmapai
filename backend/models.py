from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import SQLAlchemyError
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    mind_maps = relationship("MindMap", back_populates="owner")

class MindMap(Base):
    __tablename__ = 'mind_maps'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="mind_maps")

def create_database():
    engine = create_engine(DATABASE_URL)
    try:
        Base.metadata.create_all(bind=engine)
        print("Database and tables created successfully.")
    except SQLAlchemyError as e:
        print(f"Error creating database: {e}")

if __name__ == "__main__":
    create_database()