from pydantic import BaseModel


class GetAiChatResponseOutput(BaseModel):
    response: str


class GetChatStatusTodayOutput(BaseModel):
    user_name: str
    chat_cnt: int


class UserChatMessage(BaseModel):
    type: str
    text: str


type GetUserChatHistoryOutput = list[UserChatMessage]


# class UserConversationMessages(BaseModel):
#     user_id: ObjectIdField = Field()
#     user_name: str = Field()
#     conversation_id: ObjectIdField = Field(default=None)
#     title: str = Field()
#     created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
#     created_by: ObjectIdField = Field()
#     updated_at: Optional[datetime.datetime] = Field(default=None)
#     updated_by: Optional[ObjectIdField] = Field(default=None)
#     messages: list[Message]
