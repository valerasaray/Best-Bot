from random import choice as rc
import pyttsx3 as audio
from random import randint as ri
from datetime import datetime
from cryptocompare import get_price as gp

sorry = ['Пожалуйста, повторите ещё раз', 'Изивините, я не понимаю', 'Не знаю, что и ответить',
         'Понять подобное выше моих сил!', 'Простите, что вы сказали? Я не совсем уловил мысль']

hi = ['Здравствуйте! Рад вас видеть! Как ваши дела?', 'Привет, дружище, чем могу быть полезен?',
      'Эх, опять работать заставят... Ой, извините, не знал, что запись уже работает...',
      'Привет, чем займемся в этот раз?', 'Здравствуй, друг', 'Все команды к вашим услугам']

hours = ['час', 'часа', 'часов']

mins = ['минута', 'минуты', 'минуты']

secs = ['секунда', 'секунды', 'секунд']

days = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое',
        'девятое', 'десятое', 'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое',
        'пятнадцатое', 'шестнадцатое', 'семнадцатое', 'восемнадцатое', 'девятнадцатое',
        'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье',
        'двадцать четвертое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое',
        'двадцать девятое', 'тридцатое', 'тридцать первое']

month = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа',
         'сентября', 'октября', 'ноября', 'декабря']


def voice(v):
    sound = audio.init()
    sound.say(v)
    sound.runAndWait()


def random_number(x):
    a = 0
    b = 100
    n = True
    x = x.split()
    for i in x:
        if i.isdigit():
            if n:
                b = int(i)
                n = False
            else:
                a = b
                b = int(i)
                break

    y = f'Вот ваше рандомное число от {a} до {b}'
    voice(y)
    return ri(a, b)


def clock(x):
    time = datetime.now()

    if time.hour == 1:
        h = hours[0]
    elif time.hour < 5:
        h = hours[1]
    else:
        h = hours[2]

    if time.minute == 1:
        m = mins[0]
    elif time.minute < 5:
        m = mins[1]
    else:
        m = mins[2]

    if time.second == 1:
        s = secs[0]
    elif time.second < 5:
        s = secs[1]
    else:
        s = secs[2]

    y = f'Сейчас {time.hour} {h} {time.minute} {m} {time.second} {s}'
    voice(y)
    return f'Сейчас {time.hour}:{time.minute}:{time.second}'


def calendar(x):
    date = datetime.now()
    y = f'Сегодня {days[date.day - 1]} {month[date.month - 1]}'
    voice(y)
    return y


def repeat(x):
    x = x.split()
    x.remove('повтори')
    print(x)
    y = ''.join(x)
    voice(y)
    return y


def unknown(x):
    y = rc(sorry)
    voice(y)
    return y


def hello(x):
    y = rc(hi)
    voice(y)
    return y


def name(x):
    y = 'Меня зовут Бэст Бот. Я голосовой ассистент и создан для сдачи реферата. ' \
        'Люблю мемы, пайтон и отвечать на ваши вопросы.' \
        'В мою душу вложили старание и ненависть к двести пятьдесят восьмому чекеру.' \
        'А вас как зовут?'
    voice(y)
    return 'Меня зовут Best Bot. Я голосовой ассистент и создан для сдачи реферата. ' \
        'Люблю мемы, python и отвечать на ваши вопросы' \
        'В мою душу вложили старание и ненависть к 258 чекеру' \
        'А вас как зовут?'


def your_name(x):
    y = f'Приятно познакомиться. Что я могу для вас сделать?'
    voice(y)
    return y


def crypto(x):
    if 'эф' in x or 'еф' in x:
        price = gp('ETH', currency='USD')['ETH']['USD']
        n = 'эфириума'
    else:
        price = gp('BTC', currency='USD')['BTC']['USD']
        n = 'биткойна'
    y = f'Цена {n} на данный момент составляет {round(int(price))} долларов'
    voice(y)
    return y


def helper(x):
    y = 'Я умею общаться, могу подсказать который час и какое сегодня число. ' \
        'Знаю курс криптовалют и смогу назвать случайное число, обращайтесь!'
    voice(y)
    return y