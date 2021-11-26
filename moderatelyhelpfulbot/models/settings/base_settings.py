from models.settings import ModMail, PostRestriction
from pydantic.dataclasses import dataclass


@dataclass
class BaseSettings:
    post_restriction: PostRestriction
    modmail: ModMail
