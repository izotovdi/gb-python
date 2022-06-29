my_list = [7, 5, 3, 3, 2]
print(my_list)

while True:
    new_value = input("Введите число >>> ")

    if not new_value.isdigit():
        print("Неверный формат числа")
        exit()

    new_value = int(new_value)
    list_len = len(my_list)

    for i in range(0, list_len):
        if i + 1 == list_len:
            my_list.append(new_value)
            break

        if my_list[i] == new_value and my_list[i + 1] != new_value:
            my_list.insert(i + 1, new_value)
            break

        if my_list[i] < new_value:
            my_list.insert(i, new_value)
            break

    # решение методом сортировки
    # my_list.append(new_value)
    # my_list.sort()
    # my_list.reverse()

    print(my_list)
