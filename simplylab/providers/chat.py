import datetime
from typing import Optional

import pymongo
from loguru import logger

from simplylab.database import Database
from simplylab.model.table import ObjectIdField
from simplylab.model.table import Message


class ChatProvider:
    def __init__(self, db: Database) -> None:
        self.db = db

    async def check_user_message_limited_in_30_seconds(self, user_id: ObjectIdField) -> bool:
        time_start = datetime.datetime.now() - datetime.timedelta(seconds=30)
        count = await self.db.message.count_documents({
            "user_id": user_id,
            "type": "user",
            "created_at": {"$gte": time_start}
        })
        if count > 3:
            return True
        return False

    async def check_user_message_limited_in_daily(self, user_id: ObjectIdField) -> bool:
        today_start = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        count = await self.db.message.count_documents({
            "user_id": user_id,
            "type": "user",
            "created_at": {"$gte": today_start}
        })
        if count > 20:
            return True
        return False

    async def add_chat_message(self, messages: list[Message]) -> int:
        res = await self.db.message.insert_many(documents=[msg.model_dump(by_alias=True) for msg in messages])
        return len(res.inserted_ids)

    async def get_user_chat_messages(self, user_id: ObjectIdField, limit: int = 10) -> Optional[list[Message]]:
        logger.debug(f"user_id={user_id}, limit={limit}")
        messages = await (self.db.message.find({"user_id": user_id})
                          .sort("created_at", pymongo.DESCENDING)
                          .limit(limit=limit).to_list(limit))
        logger.info(f"Found {len(messages)} messages")
        if not messages:
            return []
        msgs = []
        for message in messages:
            msgs.append(Message(**message))
        return msgs

    async def get_user_chat_messages_count_today(self, user_id: ObjectIdField) -> int:
        today_start = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        count = await self.db.message.count_documents({
            "user_id": user_id,
            "type": "user",
            "created_at": {"$gte": today_start}
        })
        logger.info(f"count: {count}")
        return count
