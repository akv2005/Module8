class MyException1(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info

class MyException2(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info

def f(a,b):
    if b == 0:
        raise MyException1(message='Деление на ноль не возможно', extra_info= {'a': a ,'b': b})
    return a/b

def MyException2(a, b):
    try:
        a + b
    except TypeError:
        return a, b
    else:
        return a + b


try:
    resalt = f(10, 0)
    print(resalt)
except MyException1 as e:
    print("поймали ошибку")
    print(f'ошибка{e.message}')
    print(f'Дополнительная инфа {e.extra_info}')

