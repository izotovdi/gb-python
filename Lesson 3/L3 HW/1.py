def divide(x, y):
    """
    Функция деления
    :param x: делимое
    :param y: делитель
    :return: результат деления
    """
    x = float(x)
    y = float(y)

    if y != 0:
        return x / y
    else:
        print("На 0 делить нельзя")
        return None


while True:
    a, b = input("Bедите данные для выполнения деления через пробел:>>>").split()
    print(f"Результат: {a} / {b} = {divide(a, b)}")
