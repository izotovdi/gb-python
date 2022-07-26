# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

user_data = {'uname': 'Имя', 'ulname': "Фамилия", 'bdate': "Год рождения", 'city': "Город проживания", 'email': "email",
             'phone': "Телефон"}

tmp_dict = dict()   #переменная для хранения данных о пользователе


def user_info(uname, ulname, bdate, city, email, phone):
    """
    Функция принимает параметры пользователя и выводит данные одной строкой
    :param uname: Имя
    :param ulname: Фамилия
    :param bdate: Год Рождения
    :param city: Город
    :param email: email
    :param phone: телефон
    """
    print(f"{uname} {ulname}, {bdate} года рождения, проживает в {city}. Телефон для связи {phone}, e-mail: {email}")


for key, val in user_data.items():
    tmp_dict.update({key: input(f"{val} >>> ")})

user_info(*tmp_dict.values())

# Если выполнять функцию с обращением по имени то:
#
# user_info(
#     ulname=tmp_dict.get("ulname"),
#     uname=tmp_dict.get("uname"),
#     bdate=tmp_dict.get("bdate"),
#     city=tmp_dict.get("city"),
#     email=tmp_dict.get("email"),
#     phone=tmp_dict.get("phone")
# )
