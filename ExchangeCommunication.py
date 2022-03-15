from time import sleep
from httplib2 import Response
import requests
import os

class ExchangeCommunicator:
    def __init__(self, from_c, *targets) -> None:
        self.exchange_url = os.environ["EXCHANGE_URL"]
        self.api_key = os.environ["API_KEY"]
        self.sleep_time = int(os.environ["CALL_TIMEOUT"])
        self.listen = True
        self.from_c = from_c
        self.targets = targets

    @property
    def from_c(self):
        return self._from_c
    @from_c.setter
    def from_c(self, from_c):
        if from_c:
            self._from_c = from_c
        else:
            raise ValueError("base currency can't be null".upper())

    @property
    def targets(self):
        return self._targets
    @targets.setter
    def targets(self, *targets):
        self._targets = set(*targets)

    def __eq__(self, other):
        return self.from_c == other.from_c and self.targets == other.targets

    def __construct_url__(self):
        url = f"{self.exchange_url}/?api_key={self.api_key}&base={self.from_c}"
        return url + f"&target={','.join(self.targets)}" if self.targets else url

    def __repr__(self) -> str:
        return self._from_c

    def __str__(self) -> str:
        return self._from_c

    def request_rates(self):
        while self.listen:
            result : Response = requests.request(url=self.__construct_url__(), method="GET")
            print(result.status_code)
            print(result.content)
            sleep(self.sleep_time)
