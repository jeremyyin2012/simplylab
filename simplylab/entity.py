import datetime
from enum import Enum

from bson import ObjectId
from pydantic import BaseModel


class GetAiChatResponseInput(BaseModel):
    message: str
    user_name: str


class GetAiChatResponseOutput(BaseModel):
    response: str


class GetUserChatHistoryInput(BaseModel):
    user_name: str
    last_n: int


class UserChatMessage(BaseModel):
    type: str
    text: str


type GetUserChatHistoryOutput = list[UserChatMessage]


class GetChatStatusTodayInput(BaseModel):
    user_name: str


class GetChatStatusTodayOutput(BaseModel):
    user_name: str
    chat_cnt: int


# === mongodb documents start ===
class MessageRoleType(str, Enum):
    User = "user"
    Ai = "ai"


class User(BaseModel):
    _id: ObjectId
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class Message(BaseModel):
    _id: ObjectId
    conversation_id: ObjectId
    user_id: ObjectId
    type: MessageRoleType
    text: str
    created_at: datetime.datetime
    created_by: ObjectId
    updated_at: datetime.datetime
    updated_by: ObjectId


class Conversation(BaseModel):
    _id: ObjectId
    user_id: ObjectId
    title: str
    created_at: datetime.datetime
    created_by: ObjectId
    updated_at: datetime.datetime
    updated_by: ObjectId


# === mongodb documents end ===


class UserConversationMessages(BaseModel):
    user_id: ObjectId
    user_name: str
    conversation_id: ObjectId
    title: str
    created_at: datetime.datetime
    created_by: ObjectId
    updated_at: datetime.datetime
    updated_by: ObjectId
    messages: list[Message]


class Context(BaseModel):
    user: User
