my_list = []

while True:
    my_list.append(input("Добавте элемент в список >>> "))
    if int(input("добавить еще один элемент? 1-да / 0-нет >>>")) == 0:
        break

print(f"Исходный список : {my_list}")

for i in range(0, len(my_list) - 1):
    if i % 2 == 0:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(f"Измененный список : {my_list}")
