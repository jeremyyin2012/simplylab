class Error(Exception):
    status_code = 500


class MessageLimitedIn30SecondsError(Error):

    def __init__(self):
        super().__init__("3 messages limited in 30 seconds")
        self.status_code = 401


class MessageLimitedInDailyError(Error):

    def __init__(self):
        super().__init__("20 messages limited in daily")
        self.status_code = 401
