from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import settings

print("now creating engines....")
engine = create_engine(settings["database"]["engine"])
Base = declarative_base(bind=engine)
import models.reddit
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
s = Session()
s.rollback()
