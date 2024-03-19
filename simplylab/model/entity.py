from pydantic import BaseModel

from simplylab.model.table import User


class Context(BaseModel):
    user: User
