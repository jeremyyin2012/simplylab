from pydantic import BaseModel


class GetAiChatResponseInput(BaseModel):
    message: str
    user_name: str


class GetUserChatHistoryInput(BaseModel):
    user_name: str
    last_n: int


class GetChatStatusTodayInput(BaseModel):
    user_name: str
