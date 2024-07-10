def personal_sum(numbers):
    result = 0
    incorrect = 0
    incorrect_data = []
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect += 1
            incorrect_data.append(i)
    if incorrect_data:
        print('некорректные типы данных:', incorrect_data)
    return (result, incorrect)


def calculate_average(numbers):
    try:
        summ_ = personal_sum(numbers)
        summ = summ_[0]
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    try:
        mid = summ / (len(numbers) - summ_[1])
    except ZeroDivisionError:
        print('Деление на 0')
        return 0

    return mid


n = (1, 3, 6, 8, 9, 11)
print('среднее значение:', calculate_average(n))
n = (1, 2, 3, 4, 'five', 6)
print('среднее значение:', calculate_average(n))
n = 2
print('среднее значение:', calculate_average(n))
n = [5, 10, '10', '15']
print('среднее значение:', calculate_average(n))
n = ['25', 'six']
print('среднее значение:', calculate_average(n))
n = [0, 'zero']
print('среднее значение:', calculate_average(n))