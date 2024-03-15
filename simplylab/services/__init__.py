from typing import Any

from simplylab.entity import Context
from simplylab.providers import Providers
from simplylab.services.chat import ChatService


class Services:
    def __init__(self, ctx: Context, providers: Providers):
        self.ctx = ctx
        self.pvd = providers

    @property
    def chat(self):
        return ChatService(self.ctx, self.pvd)
