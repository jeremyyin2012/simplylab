from typing import Optional

from simplylab.entity import User


class UserProvider:

    def __init__(self):
        ...

    def get_user_by_name(self, user_name: str) -> Optional[User]:
        ...
