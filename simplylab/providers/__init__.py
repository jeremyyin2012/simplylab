from simplylab.providers.chat import ChatProvider
from simplylab.providers.openrouter import OpenRouterProvider
from simplylab.providers.user import UserProvider


class Providers:

    def __init__(self):
        ...

    @property
    def openrouter(self):
        return OpenRouterProvider()

    @property
    def user(self):
        return UserProvider()

    @property
    def chat(self):
        return ChatProvider()
