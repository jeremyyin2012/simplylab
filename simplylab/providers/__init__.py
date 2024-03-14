from simplylab.providers.openrouter import OpenRouterProvider


class Providers:

    def __init__(self):
        ...

    @property
    def openrouter(self):
        return OpenRouterProvider()
