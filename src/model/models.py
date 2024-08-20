from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

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

class CandidatesProcessed(BASE):
    __tablename__ = 'CandidatesProcessed'
    id = Column(Integer, primary_key=True, autoincrement=True)
    FullName = Column(String(MAX_STRING_SIZE), nullable=False)
    Email = Column(String(MAX_STRING_SIZE), nullable=False)
    ApplicationDate = Column(Date, nullable=False)
    CountryID = Column(Integer, ForeignKey('Countries.id'), nullable=False)
    YOE = Column(Integer, nullable=False)
    SeniorityID = Column(Integer, ForeignKey('Technologies.id'), nullable=False)
    TechonologyID = Column(Integer, ForeignKey('Seniorities.id'), nullable=False)
    CodeChallengeScore = Column(Integer, nullable=False)
    TechnicalInterviewScore = Column(Integer, nullable=False)
    Hired = Column(Integer, nullable=False)

    country = relationship("Countries", back_populates="candidates")
    seniority = relationship("Seniorities", back_populates="candidates")
    technology = relationship("Technologies", back_populates="candidates")

    def __str__ (self):
        return f" Table: {self.CandidatesProcessed.__table__}"



class Countries(BASE):
    __tablename__ = 'Countries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    CountriesName = Column(String(MAX_STRING_SIZE), nullable=False)
    
    candidates = relationship("CandidatesProcessed", back_populates="country")

    def __str__ (self):
        return f" Table: {self.Countries.__table__}"

class Technologies(BASE):
    __tablename__ = 'Technologies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    TechnologiesName = Column(String(MAX_STRING_SIZE), nullable=False)
    
    candidates = relationship("CandidatesProcessed", back_populates="technology")

    def __str__ (self):
        return f" Table: {self.Countries.__table__}"
    
class Seniorities(BASE):
    __tablename__ = 'Seniorities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    SenioritiesName = Column(String(MAX_STRING_SIZE), nullable=False)
    
    candidates = relationship("CandidatesProcessed", back_populates="seniority")

    def __str__ (self):
        return f" Table: {self.Countries.__table__}"