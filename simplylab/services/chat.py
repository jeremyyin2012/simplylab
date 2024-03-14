from typing import Any

from simplylab.entity import GetAiChatResponseInput
from simplylab.providers import Providers


class ChatService:
    def __init__(self, ctx: Any):
        self.ctx = ctx

    async def get_ai_chat_response(self, req: GetAiChatResponseInput) -> str:
        pvd = Providers()
        message = req.message
        response_content = await pvd.openrouter.chat(content=message)
        return response_content
