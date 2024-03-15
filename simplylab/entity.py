import datetime
from enum import Enum
from typing import Optional, Annotated, Any

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


from pydantic import (AfterValidator, GetPydanticSchema,
                      PlainSerializer, WithJsonSchema)
from pydantic_mongo import ObjectIdField as _objectIdField

ObjectIdField = Annotated[
    _objectIdField,
    AfterValidator(lambda id: _objectIdField(id)),
    PlainSerializer(lambda id: str(id), return_type=str, when_used='json-unless-none'),
    WithJsonSchema({'type': 'string'}, mode='serialization'),
    WithJsonSchema({'type': 'string'}, mode='validation'),
    GetPydanticSchema(lambda _s, h: h(Any))
]


class Test(BaseModel):
    id: ObjectIdField = Field(default_factory=ObjectIdField, alias='_id', title='_id')


# ObjectIdField = Annotated[str, BeforeValidator(ObjectId)]


class MessageRoleType(str, Enum):
    User = "user"
    Ai = "ai"


class User(BaseModel):
    id: ObjectIdField = Field(default_factory=ObjectIdField, alias="_id", title='_id')
    name: str = Field(min_length=3, max_length=100, description="user name")
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: Optional[datetime.datetime] = Field(default=None)

    model_config = ConfigDict(
        populate_by_name=True,
        # json_encoders={
        #     ObjectId: str,
        #     datetime: lambda dt: dt.isoformat()
        # },
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
    id: ObjectIdField = Field(default_factory=ObjectIdField, alias="_id", title='_id')
    conversation_id: ObjectIdField = Field()
    user_id: ObjectIdField = Field()
    type: MessageRoleType = Field()
    text: str = Field()
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    created_by: ObjectIdField = Field()
    updated_at: Optional[datetime.datetime] = Field(default=None)
    updated_by: Optional[ObjectIdField] = Field(default=None)

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
    id: ObjectIdField = Field(default_factory=ObjectIdField, alias="_id", title='_id')
    user_id: ObjectIdField = Field()
    title: str = Field()
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    created_by: ObjectIdField = Field()
    updated_at: Optional[datetime.datetime] = Field(default=None)
    updated_by: Optional[ObjectIdField] = Field(default=None)

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
    user_id: ObjectIdField = Field()
    user_name: str = Field()
    conversation_id: ObjectIdField = Field()
    title: str = Field()
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    created_by: ObjectIdField = Field()
    updated_at: Optional[datetime.datetime] = Field(default=None)
    updated_by: Optional[ObjectIdField] = Field(default=None)
    messages: list[Message]


class Context(BaseModel):
    user: User
