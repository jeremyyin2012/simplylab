from typing import Any

from simplylab.entity import GetAiChatResponseInput, GetUserChatHistoryInput, GetChatStatusTodayInput, UserChatMessage, \
    GetChatStatusTodayOutput, GetAiChatResponseOutput, GetUserChatHistoryOutput
from simplylab.providers import Providers


class ChatService:
    def __init__(self, ctx: Any):
        self.ctx = ctx
        self.pvd = Providers()

    async def get_ai_chat_response(self, req: GetAiChatResponseInput) -> GetAiChatResponseOutput:
        message = req.message
        response_content = await self.pvd.openrouter.chat(content=message)
        res = GetAiChatResponseOutput(response=response_content)
        return res

    async def get_user_chat_history(self, req: GetUserChatHistoryInput) -> GetUserChatHistoryOutput:
        res = [UserChatMessage(type="user", text="echo")]
        return res

    async def get_chat_status_today(self, req: GetChatStatusTodayInput) -> GetChatStatusTodayOutput:
        res = GetChatStatusTodayOutput(user_name=req.user_name, chat_cnt=0)
        return res
