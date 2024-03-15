import datetime
from enum import Enum
from typing import Optional, Annotated

from bson import ObjectId
from pydantic import BaseModel, Field, BeforeValidator, ConfigDict


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

PyObjectId = Annotated[str, BeforeValidator(ObjectId)]


class MessageRoleType(str, Enum):
    User = "user"
    Ai = "ai"


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(min_length=3, max_length=100, description="user name")
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: Optional[datetime.datetime] = Field(default=None)

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "_id": "xxx",
                "name": "jdoe",
                "created_at": datetime.datetime.now(),
                "updated_at": None,
            }
        },
    )


class Message(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    conversation_id: PyObjectId = Field()
    user_id: PyObjectId = Field()
    type: MessageRoleType = Field()
    text: str = Field()
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    created_by: PyObjectId = Field()
    updated_at: Optional[datetime.datetime] = Field(default=None)
    updated_by: Optional[PyObjectId] = Field(default=None)

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "_id": "xxx",
                "conversation_id": "xxx",
                "user_id": "xxx",
                "type": MessageRoleType.User,
                "text": "xxx",
                "created_at": datetime.datetime.now(),
                "created_by": "xxx",
                "updated_at": None,
                "updated_by": None,
            }
        },
    )


class Conversation(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: PyObjectId = Field()
    title: str = Field()
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    created_by: PyObjectId = Field()
    updated_at: Optional[datetime.datetime] = Field(default=None)
    updated_by: Optional[PyObjectId] = Field(default=None)

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "_id": "xxx",
                "user_id": "xxx",
                "title": "xx",
                "created_at": datetime.datetime.now(),
                "created_by": "xxx",
                "updated_at": None,
                "updated_by": None,
            }
        },
    )

# === mongodb documents end ===


class UserConversationMessages(BaseModel):
    user_id: PyObjectId = Field()
    user_name: str = Field()
    conversation_id: PyObjectId = Field()
    title: str = Field()
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    created_by: PyObjectId = Field()
    updated_at: Optional[datetime.datetime] = Field(default=None)
    updated_by: Optional[PyObjectId] = Field(default=None)
    messages: list[Message]


class Context(BaseModel):
    user: User
