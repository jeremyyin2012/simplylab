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
