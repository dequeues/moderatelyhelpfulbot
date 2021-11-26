from settings import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self):
        self.engine = create_engine(settings["database"]["engine"])
        self.Base = declarative_base(bind=self.engine)  # pylint:disable=invalid-name
        Session = sessionmaker(bind=self.engine)  # pylint:disable=invalid-name
        self.s = Session()  # pylint:disable=invalid-name
        self.s.rollback()

    def load_models(self):
        import models.reddit  # noqa: F401 pylint:disable=unused-import,import-outside-toplevel

        self.Base.metadata.create_all(self.engine)
        print("Loading database modules")
