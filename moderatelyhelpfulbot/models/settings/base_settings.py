from models.settings import ModMail
from models.settings import PostRestriction
from pydantic.dataclasses import dataclass


@dataclass
class BaseSettings:
    post_restriction: PostRestriction
    modmail: ModMail
