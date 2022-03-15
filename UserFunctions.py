import re

def show_elements(object):
    if isinstance(object, dict):
        for key, item in object.items():
            print(key, item[0], sep=". ")
    elif isinstance(object, list):
        for n, item in enumerate(object):
            print(n, item[0], sep=". ")
    else:
        print(object)

def get_user_action(ask_msg, actions):
    show_elements(actions)
    user_inp = input(ask_msg)
    try:
        return actions[int(user_inp)][1]
    except ValueError:
        return actions[user_inp][1]
    except (KeyError, IndexError):
        print(f"error. [{user_inp} is not a valid choice.]")

def validate_format(pattern, *currencies):
    valid = True
    for currency in currencies:
        if not re.fullmatch(pattern, currency):
            print(f"error. your currency [{currency}] is not valid".upper())
            valid = False
    return valid

def get_currency_to_watch():
    currency_regex = r"[A-Z]{3}"
    while True:
        currency = input("What currency do you want to watch? ")
        if validate_format(currency_regex, currency):
            break
    while True:
        targets = input("(Optional) Which currencies you would like to compare to? (usd,eur,huf) ")
        if not targets:
            print("Defaulting to api settings...")
            break
        targets = targets.split(",")
        if validate_format(currency_regex, *(targets)):
            break
    return (currency, targets)

