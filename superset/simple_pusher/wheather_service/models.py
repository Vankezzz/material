from sqlalchemy import Column, Integer, String, Float, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Whether(Base):
    __tablename__ = 'whether'
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    temp = Column(Float)
    time_created = Column(DateTime(timezone=True), server_default=func.now())

