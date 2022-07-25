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
    a = int(a)
    b = int(b)
    c = int(c)

    print(f"Вы ввели : {a} | {b} | {c}")

    tmp = sorted([a, b, c], reverse=True)
    summa = tmp[0] + tmp[1]
    print(f"Сумма двух наибольших элементов {tmp[0]} и {tmp[1]} равна {summa}")
    return summa


user_numbers = (input("Введите три числа через пробел >>> ")).split(" ")
my_func(user_numbers[0], user_numbers[1], user_numbers[2])
