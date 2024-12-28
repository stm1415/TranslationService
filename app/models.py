from sqlalchemy import Column, Integer, String, Text, JSON

from sqlalchemy.ext.declarative import declarative_base

# define a database table

Base = declarative_base()

class TranslationTask(Base):
    __tablename__ = "translation_tasks"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    languagues = Column(JSON, nullable=False)
    status = Column(String, default="inProgress")

    translation = Column(JSON, default={})