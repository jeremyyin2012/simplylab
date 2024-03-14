from openai import OpenAI
from os import getenv
from loguru import logger


class OpenRouterProvider:
    def __init__(self):
        ...

    async def chat(self, content: str) -> str:
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
                    "content": content,
                },
            ],
        )
        print(completion.choices[0].message.content)
        return completion.choices[0].message.content
