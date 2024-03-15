from typing import Optional

from simplylab.database import Database
from simplylab.entity import UserConversationMessages


class ChatProvider:
    def __init__(self, db: Database) -> None:
        self.db = db

    async def check_user_message_limited_in_30_seconds(self, user_id: str) -> bool:
        ...

    async def check_user_message_limited_in_daily(self, user_id: str) -> bool:
        ...

    async def get_user_conversation_messages(self, user_id, conversation_id) -> Optional[UserConversationMessages]:
        ...

    async def get_user_chat_messages_count_today(self, user_id: str) -> int:
        ...