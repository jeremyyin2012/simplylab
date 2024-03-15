import motor.motor_asyncio


class Database:
    def __init__(self, client: motor.motor_asyncio.AsyncIOMotorClient):
        self._client = client

    @property
    def user(self):
        return self._client.get_database("simplylab").get_collection("user")

    @property
    def conversation(self):
        return self._client.get_database("simplylab").get_collection("conversation")

    @property
    def message(self):
        return self._client.get_database("simplylab").get_collection("message")
