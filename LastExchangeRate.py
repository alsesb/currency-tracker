class LastExchangeRate:
    def __init__(self, from_c, to_c) -> None:
        self.from_c = from_c
        self.to_c = to_c

    @property
    def last_percentage_change(self):
        return self._last_percentage_change

    @property
    def percentage_change(self):
        return self._percentage_change
    @percentage_change.setter
    def percentage_change(self, percentage_change):
        self._last_percentage_change = self._percentage_change
        self._percentage_change = percentage_change