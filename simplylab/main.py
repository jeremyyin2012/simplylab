from typing import Union

from fastapi import FastAPI
from dotenv import load_dotenv

from simplylab.entity import GetAiChatResponseInput
from simplylab.entity import GetAiChatResponseOutput
from simplylab.entity import GetUserChatHistoryInput
from simplylab.entity import GetUserChatHistoryOutput
from simplylab.entity import GetChatStatusTodayInput
from simplylab.entity import GetChatStatusTodayOutput
from simplylab.entity import UserChatMessage
from simplylab.services import Services

load_dotenv()
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/api/v1/get_ai_chat_response")
async def get_ai_chat_response(req: GetAiChatResponseInput) -> GetAiChatResponseOutput:
    svc = Services(req)
    res = await svc.chat.get_ai_chat_response(req)
    return res


@app.post("/api/v1/get_user_chat_history")
async def get_user_chat_history(req: GetUserChatHistoryInput) -> GetUserChatHistoryOutput:
    svc = Services(req)
    res = await svc.chat.get_user_chat_history(req)
    return res


@app.post("/api/v1/get_chat_status_today")
async def get_chat_status_today(req: GetChatStatusTodayInput) -> GetChatStatusTodayOutput:
    svc = Services(req)
    res = await svc.chat.get_chat_status_today(req)
    return res
