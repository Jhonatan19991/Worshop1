from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

BASE = declarative_base()
MAX_STRING_SIZE = 100

class Candidates(BASE):
    __tablename__ = 'Candidates'
    id = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String(MAX_STRING_SIZE), nullable=False)
    LastName = Column(String(MAX_STRING_SIZE), nullable=False)
    Email = Column(String(MAX_STRING_SIZE), nullable=False)
    ApplicationDate = Column(Date, nullable=False)
    Country = Column(String(MAX_STRING_SIZE), nullable=False)
    YOE = Column(Integer, nullable=False)
    Seniority = Column(String(MAX_STRING_SIZE), nullable=False)
    Technology = Column(String(MAX_STRING_SIZE), nullable=False)
    CodeChallengeScore = Column(Integer, nullable=False)
    TechnicalInterviewScore = Column(Integer, nullable=False)
    
    def __str__ (self):
        return f" Table: {self.Candidates.__table__}"
    