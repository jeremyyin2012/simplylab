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
    response = await svc.chat.get_ai_chat_response(req)
    res = GetAiChatResponseOutput(response=response)
    return res


@app.post("/api/v1/get_user_chat_history")
async def get_user_chat_history(req: GetUserChatHistoryInput) -> GetUserChatHistoryOutput:
    res = [UserChatMessage(type="user", text="echo")]
    return res


@app.post("/api/v1/get_chat_status_today")
async def get_chat_status_today(req: GetChatStatusTodayInput) -> GetChatStatusTodayOutput:
    res = GetChatStatusTodayOutput(user_name=req.user_name, chat_cnt=0)
    return res
