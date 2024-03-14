from typing import Any

from simplylab.services.chat import ChatService


class Services:
    def __init__(self, ctx: Any):
        self.ctx = ctx

    @property
    def chat(self):
        return ChatService(self.ctx)
