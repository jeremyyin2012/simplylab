import math

from openai import OpenAI
from os import getenv
from loguru import logger

from simplylab.database import Database


def middle_out(request_content: str, model_name: str, limit: int) -> str:
    import tiktoken
    encoding = tiktoken.encoding_for_model(model_name)
    tokens = encoding.encode(request_content)
    token_count = len(tokens)
    if token_count > limit:
        rate = limit / token_count
        middle = math.floor(len(request_content) / 2)
        first_end = math.floor(middle * rate)
        second_start = math.ceil(middle + middle * (1 - rate))
        logger.debug(f"{token_count=} {limit=} {rate=} {len(request_content)=} {middle=} {first_end=} {second_start=}")
        chat_content = request_content[:first_end] + request_content[second_start:]
        return chat_content
    return request_content


class OpenRouterProvider:
    def __init__(self, db: Database) -> None:
        self.db = db

    async def chat(self, content: str) -> str:
        chat_content = middle_out(content, "gpt-3.5-turbo", 8192)
        # gets API Key from environment variable OPENAI_API_KEY
        api_key = getenv("OPENROUTER_API_KEY")
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )

        completion = client.chat.completions.create(
            extra_headers={
                # "HTTP-Referer": $YOUR_SITE_URL,  # Optional, for including your app on openrouter.ai rankings.
                # "X-Title": $YOUR_APP_NAME,  # Optional. Shows in rankings on openrouter.ai.
            },
            model="mistralai/mistral-7b-instruct:free",
            messages=[
                {
                    "role": "user",
                    "content": chat_content,
                },
            ],
        )
        logger.debug(f"request chat_content: {chat_content}")
        logger.debug(f"response content: {completion.choices[0].message.content}")
        return completion.choices[0].message.content
