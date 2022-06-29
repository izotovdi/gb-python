my_dict = [
    "зима",
    "зима",
    "весна",
    "весна",
    "весна",
    "лето",
    "лето",
    "лето",
    "осень"
    "осень"
    "осень"
    "зима",
]
select_month = input("Введите месяц в виде числа от 1 до 12 >>> ")

if not select_month.isdigit() or int(select_month) > 12:
    print("Неверный формат числа")
    exit()

select_month = int(select_month) - 1
print(my_dict[select_month])
