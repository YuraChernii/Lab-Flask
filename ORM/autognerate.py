from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.dialects.mssql import BIT, DATETIME

Base = declarative_base()
metadata = Base.metadata



class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    Moderator = Column(Boolean)
    FirstName = Column(String)
    LastName = Column(String)
    Email = Column(String)
    Password = Column(String)

class Article(Base):
    __tablename__ = 'Article'

    id = Column(Integer, primary_key=True)
    Accepted = Column(Boolean)
    NewArticle = Column(Boolean)
    Author = Column(Integer, ForeignKey("User.id"))
    Name = Column(String)
    Text = Column(Text)


engine = create_engine('mssql+pyodbc://HP-ПК/EShopDb?driver=SQL+Server+Native+Client+11.0')

Base.metadata.create_all(engine)