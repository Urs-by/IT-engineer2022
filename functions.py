from fractions import Fraction


def get_data() -> list:
    '''
    Запрашивает данные у пользователя
    :return: список данных
    '''
    a = Fraction(input('Введите первое число: '))
    op = input('Введите операцию: ')
    b = Fraction(input('Введите второе число: '))
    return [a, op, b]


def get_res_op(lst) -> str:
    '''
    Подсчитывает результат из данных
    :param lst: принемает список с данными
    :return: строку с результатом вычисления
    '''
    my_dict = {
        '*': lst[0] + lst[2],
        '/': lst[0] / lst[2],
        '+': lst[0] + lst[2],
        '-': lst[0] - lst[2]
    }
    if lst[1] in my_dict:
        return f'{lst[0]} {lst[1]} {lst[2]} = {my_dict[lst[1]]}'
    else:
        return 'Неизвестная операция!'


print(get_res_op(get_data()))

# или так можно запросить дробное число:
# a = int(input('Введите числитель: '))
# b = int(input('Введите знаменатель: '))
# ab = Fraction(a, b)
# print(ab)
