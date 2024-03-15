import os
from typing import Union
import sentry_sdk
import motor.motor_asyncio
from fastapi import FastAPI, Request
from dotenv import load_dotenv
from loguru import logger
from starlette.responses import JSONResponse

from simplylab.database import Database
from simplylab.entity import GetAiChatResponseInput, Context
from simplylab.entity import GetAiChatResponseOutput
from simplylab.entity import GetUserChatHistoryInput
from simplylab.entity import GetUserChatHistoryOutput
from simplylab.entity import GetChatStatusTodayInput
from simplylab.entity import GetChatStatusTodayOutput
from simplylab.error import Error, UserNotFoundError
from simplylab.providers import Providers
from simplylab.services import Services

load_dotenv()
sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    mongo_host = os.getenv("MONGO_HOST", "localhost")
    mongo_port = os.getenv("MONGO_PORT", "27017")
    mongo_username = os.getenv("MONGO_USERNAME")
    mongo_password = os.getenv("MONGO_PASSWORD")
    mongo_uri = f"mongodb://{mongo_username}:{mongo_password}@{mongo_host}:{mongo_port}/"
    app.mongodb_client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
    app.db = Database(client=app.mongodb_client)
    logger.info("Connected to the MongoDB database!")


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
    logger.info("Disconnected to the MongoDB database!")


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Error):
    return JSONResponse(
        status_code=500,
        content={"message": str(exc)}
    )


@app.exception_handler(Error)
async def error_handler(request: Request, exc: Error):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": str(exc)}
    )


@app.get("/")
async def hi():
    return {"Hello": "World"}


@app.post("/api/v1/get_ai_chat_response")
async def get_ai_chat_response(request: Request, req: GetAiChatResponseInput) -> GetAiChatResponseOutput:
    pvd = Providers(db=request.app.db)
    user = await pvd.user.get_user_by_name(req.user_name)
    if not user:
        raise UserNotFoundError(req.user_name)
    ctx = Context(user=user)
    svc = Services(ctx, pvd)
    res = await svc.chat.get_ai_chat_response(req)
    return res


@app.post("/api/v1/get_user_chat_history")
async def get_user_chat_history(request: Request, req: GetUserChatHistoryInput) -> GetUserChatHistoryOutput:
    pvd = Providers(db=request.app.db)
    user = await pvd.user.get_user_by_name(req.user_name)
    if not user:
        raise UserNotFoundError(req.user_name)
    ctx = Context(user=user)
    svc = Services(ctx, pvd)
    res = await svc.chat.get_user_chat_history(req)
    return res


@app.post("/api/v1/get_chat_status_today")
async def get_chat_status_today(request: Request, req: GetChatStatusTodayInput) -> GetChatStatusTodayOutput:
    pvd = Providers(db=request.app.db)
    user = await pvd.user.get_user_by_name(req.user_name)
    if not user:
        raise UserNotFoundError(req.user_name)
    ctx = Context(user=user)
    svc = Services(ctx, pvd)
    res = await svc.chat.get_chat_status_today(req)
    return res
