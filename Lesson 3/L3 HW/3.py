# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(a, b, c):
    """
    Принимает три аргумента,и возвращает сумму наибольших двух аргументов
    :param a: Аргумент 1
    :param b: Аргумент 2
    :param c: Аргумент 3
    :return:
    """
    tmp = [a, b, c]
    top, down = a, a

    for i in tmp:
        if i > top:
            top = i
        if i < down:
            down = i

    summa = top + down
    print(f"{top} + {down} = {summa}")

    return summa


print("Функция возвращает значение : ", my_func(a=2, b=10, c=12))
