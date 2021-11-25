from datetime import datetime

from sqlalchemy import Column, DateTime, String

from core import dbobj


class LoggedActions(dbobj.Base):
    __tablename__ = "Actions"
    subreddit_name = Column(String(21), nullable=True)
    action_id = Column(String(30), nullable=True, primary_key=True)
    date_actioned = Column(DateTime, nullable=True)

    def __init__(
            self,
            comment_id,
    ):
        self.comment_id = comment_id
        self.date_actioned = datetime.now()
