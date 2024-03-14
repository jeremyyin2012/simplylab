from typing import Union

from fastapi import FastAPI

from .entity import GetAiChatResponseInput
from .entity import GetAiChatResponseOutput
from .entity import GetUserChatHistoryInput
from .entity import GetUserChatHistoryOutput
from .entity import GetChatStatusTodayInput
from .entity import GetChatStatusTodayOutput
from .entity import UserChatMessage

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/api/v1/get_ai_chat_response")
async def get_ai_chat_response(req: GetAiChatResponseInput) -> GetAiChatResponseOutput:
    res = GetAiChatResponseOutput(response="Hello World")
    return res


@app.post("/api/v1/get_user_chat_history")
async def get_user_chat_history(req: GetUserChatHistoryInput) -> GetUserChatHistoryOutput:
    res = [UserChatMessage(type="user", text="echo")]
    return res


@app.post("/api/v1/get_chat_status_today")
async def get_chat_status_today(req: GetChatStatusTodayInput) -> GetChatStatusTodayOutput:
    res = GetChatStatusTodayOutput(user_name=req.user_name, chat_cnt=0)
    return res
