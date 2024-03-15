from simplylab.database import Database
from simplylab.providers.chat import ChatProvider
from simplylab.providers.openrouter import OpenRouterProvider
from simplylab.providers.user import UserProvider


class Providers:

    def __init__(self, db: Database) -> None:
        self.db = db

    @property
    def openrouter(self):
        return OpenRouterProvider(db=self.db)

    @property
    def user(self):
        return UserProvider(db=self.db)

    @property
    def chat(self):
        return ChatProvider(db=self.db)
