import eel
from functions import random_number, clock, calendar, unknown, hello, name, your_name, crypto, helper, repeat

eel.init("web")


@eel.expose()
def f(x):
    x = x.lower()
    print(x)
    if ('ран' in x or 'сл' in x) and "чис" in x:
        return random_number(x)
    elif 'врем' in x or 'котор' in x:
        return clock(x)
    elif 'дат' in x or 'кал' in x or 'чис' in x or 'сег' in x:
        return calendar(x)
    elif 'пр' in x or 'зд' in x or 'ха' in x or 'хэ' in x or 'хе' in x or 'эй' in x:
        return hello(x)
    elif 'как' in x and ('им' in x or 'зов' in x):
        return name(x)
    elif ('мо' in x or 'зов' in x) and ('им' in x or 'зов' in x):
        return your_name(x)
    elif 'повтори' in x:
        return repeat(x)
    if 'кур' in x or 'цен' in x or 'би' in x or 'эф' in x or 'еф' in x:
        return crypto(x)
    elif 'пом' in x or 'ком' in x or 'мож' in x or 'ум' in x:
        return helper(x)
    return unknown(x)


eel.start("main.html", size=(500, 800))
