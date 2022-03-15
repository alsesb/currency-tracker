from concurrent.futures import ThreadPoolExecutor
import os
import sys

from ExchangeCommunication import ExchangeCommunicator
from UserFunctions import get_currency_to_watch, get_user_action

# GLOBAL VARIABLES
MAXIMUM_WATCHERS = int(os.environ["THREAD_POOL"])
WATCHING_FOR = []
EXECUTOR = ThreadPoolExecutor(max_workers=MAXIMUM_WATCHERS, thread_name_prefix="CURRENCY_LISTENER")

# FUNCTIONALITY
def add_currency_to_watch():
    base, targets = get_currency_to_watch()
    WATCHING_FOR.append(ExchangeCommunicator(base, *targets))
    EXECUTOR.submit(lambda: WATCHING_FOR[-1].request_rates())
    print(f"Now watching the following currencies: {WATCHING_FOR}")

FUNCTIONS = {
    1: ("Add new exchange rate to watch", add_currency_to_watch),
    2: ("Exit", sys.exit)
}

# MAIN
def main():
    while True:
        get_user_action("What would you like to do? ", FUNCTIONS)()

# ONLY RUN IF NECESSARY
if __name__ == "__main__":
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
    main()