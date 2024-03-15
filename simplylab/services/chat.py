from typing import Any

from loguru import logger

from simplylab.entity import GetAiChatResponseInput, GetUserChatHistoryInput, GetChatStatusTodayInput, UserChatMessage, \
    GetChatStatusTodayOutput, GetAiChatResponseOutput, GetUserChatHistoryOutput, Context, Message, MessageRoleType
from simplylab.error import MessageLimitedInDailyError, MessageLimitedIn30SecondsError
from simplylab.providers import Providers


class ChatService:
    def __init__(self, ctx: Context, provider: Providers):
        self.ctx = ctx
        self.pvd = provider

    async def get_ai_chat_response(self, req: GetAiChatResponseInput) -> GetAiChatResponseOutput:
        if self.pvd.chat.check_user_message_limited_in_30_seconds(self.ctx.user.id):
            raise MessageLimitedIn30SecondsError()
        if self.pvd.chat.check_user_message_limited_in_daily(self.ctx.user.id):
            raise MessageLimitedInDailyError()

        request_content = req.message
        # todo: request content middle out
        response_content = await self.pvd.openrouter.chat(content=request_content)
        user_message = Message(
            user_id=self.ctx.user.id,
            type=MessageRoleType.User,
            text=request_content,
            created_by=self.ctx.user.id,
        )
        ai_message = Message(
            user_id=self.ctx.user.id,
            type=MessageRoleType.Ai,
            text=response_content,
            created_by=self.ctx.user.id,
        )
        messages = [user_message, ai_message]
        count = await self.pvd.chat.add_chat_message(messages=messages)
        logger.debug(f"Added {count} chat messages")
        res = GetAiChatResponseOutput(response=response_content)
        return res

    async def get_user_chat_history(self, req: GetUserChatHistoryInput) -> GetUserChatHistoryOutput:
        messages = await self.pvd.chat.get_user_chat_messages(user_id=self.ctx.user.id, limit=req.last_n)
        res = []
        for message in messages:
            res.append(UserChatMessage(type=message.type.value, text=message.text))
        return res

    async def get_chat_status_today(self, req: GetChatStatusTodayInput) -> GetChatStatusTodayOutput:
        count = await self.pvd.chat.get_user_chat_messages_count_today(user_id=self.ctx.user.id)
        res = GetChatStatusTodayOutput(user_name=self.ctx.user.name, chat_cnt=count)
        return res
