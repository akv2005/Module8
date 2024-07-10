#Регистрация в клуб любителей Пива

class MyException1(Exception):
    pass

class MyException2(Exception):
    pass

class MyException3(Exception):
    pass

def Веек_club():
    print('---Регистрация в клуб любителей Пива---')
    name_ = str(input('Ваше имя?: '))
    beer_love = str(input('Пиво уважеете?: (Да, нет) '))
    try:
        if beer_love == 'нет':
            raise MyException1("Вам не место в клубе!!!")
    except MyException1 as exc1:
        print(f'Ошибка: {exc1}')
        raise
    else:
        print(f'{beer_love} - Пока подходите, но есть еще несколько вопросов')

    beer_age = int(input('Введите возраст: '))
    try:
        if beer_age <= 21:
            raise MyException2("Тебе еще только лимонад можно.")
    except MyException2 as exc2:
        print(f'Ошибка: {exc2}')
        raise
    else:
        print("Пока подходишь!")

    beer_valume = int(input('Сколько кружек можешь выпить за один раз?: '))
    try:
        if beer_valume < 3:
            raise MyException3("Ты нам не очень нравишься, нужно пить больше.")
    except MyException3 as exc3:
        print(f'Ошибка: {exc3}')
        raise
    else:
        print("Ок, ждем тебя в клубе")
    finally:
        print(f'Спасибо, {name_}! Ты ответил на все вопросы!')


Веек_club()
